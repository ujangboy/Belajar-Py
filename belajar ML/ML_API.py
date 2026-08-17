import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# 1. Data latihan sederhana (Teks & Label: 1 = Positif, 0 = Negatif)
data_teks = [
    "Saya sangat suka aplikasi ini, keren sekali!",
    "Bagus banget, sangat membantu pekerjaan saya.",
    "Aplikasi ini jelek, sering error dan lambat.",
    "Sangat kecewa, layanannya buruk sekali.",
    "Mantap, berfungsi dengan baik!",
    "Sama sekali tidak berguna, buang-buang waktu.",
]
labels = [1, 1, 0, 0, 1, 0]

# 2. Membuat Pipeline (Mengubah teks ke angka + Model Logistic Regression)
model_pipeline = Pipeline(
    [("vectorizer", CountVectorizer()), ("classifier", LogisticRegression())]
)

# 3. Latih model
model_pipeline.fit(data_teks, labels)

# 4. Simpan model yang sudah pintar ke dalam file
joblib.dump(model_pipeline, "model_sentimen.pkl")
print("Model berhasil dilatih dan disimpan sebagai 'model_sentimen.pkl'!")