import os
import json
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_absolute_error, r2_score, accuracy_score, classification_report

# 1. Pastikan folder models/ ada
os.makedirs("models", exist_ok=True)

# 2. Muat dataset
dataset_path = "student_dataset_10000_rows.csv"
print(f"Memuat data dari {dataset_path}...")
df = pd.read_csv(dataset_path)

# 3. Definisikan Fitur dan Target
feature_cols = [
    "study_hours",
    "attendance",
    "sleep_hours",
    "internet_usage",
    "assignments_completed",
    "previous_score"
]

X = df[feature_cols]
y_reg = df["exam_score"]
y_clf = df["placement_status"].map({"Placed": 1, "Not Placed": 0})

# Split data (80% train, 20% test)
X_train, X_test, y_reg_train, y_reg_test = train_test_split(
    X, y_reg, test_size=0.2, random_state=42
)
_, _, y_clf_train, y_clf_test = train_test_split(
    X, y_clf, test_size=0.2, random_state=42
)

# 4. Latih Regressor (Exam Score)
print("Melatih model RandomForestRegressor untuk prediksi Exam Score...")
reg_model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
reg_model.fit(X_train, y_reg_train)

# Evaluasi Regressor
y_reg_pred = reg_model.predict(X_test)
mae = mean_absolute_error(y_reg_test, y_reg_pred)
r2 = r2_score(y_reg_test, y_reg_pred)
print(f"Evaluasi Regressor -> MAE: {mae:.4f}, R2 Score: {r2:.4f}")

# 5. Latih Classifier (Placement Status)
print("Melatih model RandomForestClassifier untuk prediksi Placement Status...")
clf_model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
clf_model.fit(X_train, y_clf_train)

# Evaluasi Classifier
y_clf_pred = clf_model.predict(X_test)
accuracy = accuracy_score(y_clf_test, y_clf_pred)
print(f"Evaluasi Classifier -> Accuracy: {accuracy:.4f}")
print(classification_report(y_clf_test, y_clf_pred))

# 6. Simpan Model
print("Menyimpan model ke folder 'models'...")
joblib.dump(reg_model, "models/exam_score_model.pkl")
joblib.dump(clf_model, "models/placement_model.pkl")

# 7. Ambil Feature Importance
reg_importance = reg_model.feature_importances_
clf_importance = clf_model.feature_importances_

# Buat dictionary metrics untuk digunakan di frontend
metrics = {
    "regression": {
        "mae": float(mae),
        "r2": float(r2),
        "feature_importances": {col: float(imp) for col, imp in zip(feature_cols, reg_importance)}
    },
    "classification": {
        "accuracy": float(accuracy),
        "feature_importances": {col: float(imp) for col, imp in zip(feature_cols, clf_importance)}
    }
}

# Simpan metrics ke json
metrics_path = "models/metrics.json"
with open(metrics_path, "w") as f:
    json.dump(metrics, f, indent=4)
print(f"Metrik model berhasil disimpan ke {metrics_path}!")
print("Proses training selesai!")
