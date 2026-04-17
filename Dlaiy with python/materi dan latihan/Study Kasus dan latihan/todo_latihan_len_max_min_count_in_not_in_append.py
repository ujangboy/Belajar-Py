# Operasi List, Set, dan String

"""len() = mengihitung jumlah total elemen
max() = mengembalikan nilai terbesar dari sekumlupan data atau elemen
min() = mengembalikan nilai terkecil dari sekumpulan data atau elemen
count() = menghitung jumlah kemunculan elemen tertentu dalam list atau string
in() = memeriksa apakah elemen tertentu ada dalam list, set, atau string
not in() = memeriksa apakah elemen tertentu tidak ada dalam list, set, atau string
append() = menambahkan elemen baru di akhir list"""
# ================================
# TODO 1: PANJANG DATA
# ================================
# Soal: Hitung jumlah karakter dalam string "python programming"
# Tambahkan kode Anda di sini:

text1 = "python programming"
# Jawaban Anda:
print(len(text1))

print("=" * 50)

# ================================
# TODO 2: NILAI TERBESAR
# ================================
# Soal: Temukan nilai terbesar dari list berikut
# Tambahkan kode Anda di sini:

numbers1 = [10, 25, 8, 42, 33, 17]
# Jawaban Anda:
nilai_terbesar = max(numbers1)
print(nilai_terbesar)

print("=" * 50)

# ================================
# TODO 3: NILAI TERKECIL
# ================================
# Soal: Temukan nilai terkecil dari list berikut
# Tambahkan kode Anda di sini:

numbers2 = [100, 25, 8, 42, 33, 17]
# Jawaban Anda:
nilai_terkecil =min(numbers2)
print(nilai_terkecil)

print("=" * 50)

# ================================
# TODO 4: HITUNG KEMUNCULAN
# ================================
# Soal: Hitung berapa kali huruf 'a' muncul dalam string berikut
# Tambahkan kode Anda di sini:

text2 = "algorithm and data analysis"
# Jawaban Anda:
jumlah_a = text2.count("a")
print(jumlah_a)

print("=" * 50)

# ================================
# TODO 5: CEK ELEMEN DALAM LIST
# ================================
# Soal: Cek apakah 'python' ada dalam list berikut
# Tambahkan kode Anda di sini:

languages = ["java", "python", "javascript", "go"]
# Jawaban Anda:
mengecek_python = "python" in languages
print(mengecek_python)

print("=" * 50)

# ================================
# TODO 6: CEK ELEMEN TIDAK ADA
# ================================
# Soal: Cek apakah 'rust' TIDAK ADA dalam list berikut
# Tambahkan kode Anda di sini:

languages = ["java", "python", "javascript", "go"]
# Jawaban Anda:
mengecek_rust = "rust" not in languages
print(mengecek_rust)

print("=" * 50)

# ================================
# TODO 7: TAMBAHKAN KE LIST
# ================================
# Soal: Tambahkan 'rust' ke dalam list berikut
# Tambahkan kode Anda di sini:

languages = ["java", "python", "javascript", "go"]
# Jawaban Anda:
# menambahkan di seteah java
menambah_rust = languages.append("rust")
print(languages)

print("=" * 50)

# ================================
# TODO 8: JUMLAH KATA DALAM LIST
# ================================
# Soal: Hitung jumlah elemen dalam list berikut
# Tambahkan kode Anda di sini:

words = ["hello", "world", "python", "code", "learning"]
# Jawaban Anda:
jumlahElemen = len(words)
print(jumlahElemen)

print("=" * 50)

# ================================
# TODO 9: NILAI TERTINGGI DARI STRING
# ================================
# Soal: Temukan karakter dengan nilai ASCII tertinggi dalam string berikut
# Tambahkan kode Anda di sini:

text3 = "python"
# Jawaban Anda:
nilai_ascii_tertinggi = max(text3)
print(nilai_ascii_tertinggi)

print("=" * 50)

# ================================
# TODO 10: HITUNG KEMUNCULAN KATA
# ================================
# Soal: Hitung berapa kali kata 'python' muncul dalam list berikut
# Tambahkan kode Anda di sini:

words_list = ["python", "java", "python", "go", "python", "rust"]
# Jawaban Anda:
jumlah_pytronMUncul = words_list.count("python")
print(jumlah_pytronMUncul)

print("=" * 50)
print("LATIHAN KOKMBISANASI")
print("=" * 50)

# ================================
# TODO 1: ANALISIS STRING
# ================================
# Soal: Dari string berikut:
#       - Hitung jumlah karakter
#       - Temukan karakter dengan nilai tertinggi (menggunakan max)
#       - Cek apakah mengandung huruf 'a'
# Input:
text1 = "algorithm"
# Jawaban Anda:
jumlah_karekter = len(text1)
nilai_tertinggi = max(text1)
mengandung_a = 'a' in text1

print(jumlah_karekter)
print(nilai_tertinggi)
print(mengandung_a)

print("=" * 50)

# ================================
# TODO 2: FILTER DAN TAMBAHKAN
# ================================
# Soal: Dari list berikut:
#       - Tambahkan elemen "ruby" jika "ruby" tidak ada di dalam list
#       - Hitung jumlah kemunculan "python"
# Input:
langs = ["python", "java", "go", "python", "javascript"]
# Jawaban Anda:

if "ruby" not in langs:
    langs.append("ruby")
jumlah_python = langs.count("python")   

print(langs)
print(jumlah_python)

print("=" * 50)

# ================================
# TODO 3: NILAI EKSTREM DALAM LIST
# ================================
# Soal: Dari list berikut:
#       - Cari nilai terbesar dan terkecil
#       - Hitung jumlah elemen
# Input:
numbers = [12, 45, 7, 23, 89, 4]
# Jawaban Anda:
nilai_terkecil = min(numbers)
jumlah_elemen = len(numbers)

print(nilai_terkecil)
print(jumlah_elemen)

print("=" * 50)

# ================================
# TODO 4: CEK & HITUNG KEMUNCULAN
# ================================
# Soal: Dari list berikut:
#       - Cek apakah "hello" ada di dalam list
#       - Hitung berapa kali "hello" muncul
# Input:
words = ["hello", "world", "hello", "python", "hello"]
# Jawaban Anda:
mengecek_hello = "hello" in words
jumlah_hello = words.count("hello")

print(mengecek_hello)
print(jumlah_hello)

print("=" * 50)

# ================================
# TODO 5: MANIPULASI LIST
# ================================
# Soal: Dari list berikut:
#       - Tambahkan "rust" jika "rust" tidak ada di dalam list
#       - Hitung jumlah elemen setelah ditambahkan
# Input:
tech_list = ["python", "go", "javascript"]
# Jawaban Anda:
if "rust" not in tech_list:
    tech_list.append("rust")
jumlah_elemen = len(tech_list)

print(tech_list)
print(jumlah_elemen)

print("=" * 50)