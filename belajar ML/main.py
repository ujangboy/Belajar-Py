import os
import json
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

app = FastAPI(
    title="Dashboard Prediktif Performa Siswa",
    description="API untuk memprediksi nilai ujian siswa dan status penempatan kerja.",
)

# Cek apakah model sudah dibuat
if not os.path.exists("models/exam_score_model.pkl") or not os.path.exists("models/placement_model.pkl"):
    raise RuntimeError("Model belum dilatih! Jalankan train_models.py terlebih dahulu.")

# Muat model
reg_model = joblib.load("models/exam_score_model.pkl")
clf_model = joblib.load("models/placement_model.pkl")

class StudentInput(BaseModel):
    study_hours: int = Field(..., ge=1, le=11, description="Jam belajar per hari (1-11)")
    attendance: int = Field(..., ge=40, le=100, description="Persentase kehadiran (40-100)")
    sleep_hours: int = Field(..., ge=4, le=9, description="Jam tidur per hari (4-9)")
    internet_usage: int = Field(..., ge=1, le=11, description="Skala penggunaan internet (1-11)")
    assignments_completed: int = Field(..., ge=0, le=20, description="Jumlah tugas diselesaikan (0-20)")
    previous_score: int = Field(..., ge=35, le=95, description="Nilai ujian sebelumnya (35-95)")

@app.post("/api/predict")
def predict(data: StudentInput):
    # Buat DataFrame dari input
    input_df = pd.DataFrame([{
        "study_hours": data.study_hours,
        "attendance": data.attendance,
        "sleep_hours": data.sleep_hours,
        "internet_usage": data.internet_usage,
        "assignments_completed": data.assignments_completed,
        "previous_score": data.previous_score
    }])
    
    # Prediksi Exam Score
    predicted_score = float(reg_model.predict(input_df)[0])
    
    # Prediksi Placement Probability
    placement_probs = clf_model.predict_proba(input_df)[0]
    placement_prob = float(placement_probs[1]) # probability of class 1 (Placed)
    
    # Tentukan status berdasarkan probabilitas / prediksi langsung
    predicted_class = int(clf_model.predict(input_df)[0])
    placement_status = "Placed" if predicted_class == 1 else "Not Placed"
    
    return {
        "predicted_exam_score": round(predicted_score, 2),
        "placement_probability": round(placement_prob, 4),
        "placement_status": placement_status
    }

@app.get("/api/metrics")
def get_metrics():
    metrics_path = "models/metrics.json"
    if not os.path.exists(metrics_path):
        raise HTTPException(status_code=404, detail="File metrik belum tersedia.")
    with open(metrics_path, "r") as f:
        metrics = json.load(f)
    return metrics

# Mount folder static untuk file frontend (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return FileResponse("static/index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)