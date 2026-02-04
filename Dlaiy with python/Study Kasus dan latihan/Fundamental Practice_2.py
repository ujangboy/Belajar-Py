"""
================================================================================
SOAL LATIHAN FUNDAMENTAL PYTHON - KOMBINASI & LOGIKA
================================================================================
Latihan ini dirancang untuk mengasah logika dan menggabungkan berbagai konsep dasar Python.
Selesaikan setiap soal dan gunakan print() untuk menampilkan hasil.
================================================================================
"""

# ============================================================================
# BAGIAN 1: KOMBINASI VARIABEL, OPERASI & STRING
# ============================================================================

# Soal 1: Kombinasi Umur dan Nama
# Diberi variabel: nama = "Andi", umur = 17, tinggi = 172.5
# Buat output dalam format: "Halo, saya Andi berumur 17 tahun dengan tinggi 172.5 cm."
# TODO: Tulis kode Anda di bawah


# Soal 2: Konversi Suhu
# Diberi suhu dalam Celsius: 25 derajat
# Konversi ke Fahrenheit: (C * 9/5) + 32
# Tampilkan: "25°C sama dengan ...°F"
# TODO: Tulis kode Anda di bawah


# ============================================================================
# BAGIAN 2: KOMBINASI LIST & KONDISIONAL
# ============================================================================

# Soal 3: Analisis Nilai Siswa
# Diberi list nilai: [85, 92, 78, 60, 45, 88, 76, 95, 50]
# a) Cetak semua nilai
# b) Kelompokkan nilai menjadi: "Lulus (>75)" dan "Remedial (≤75)"
# c) Cetak berapa banyak siswa yang lulus dan remedial
# TODO: Tulis kode Anda di bawah


# Soal 4: Pencarian & Manipulasi List
# Diberi list buah: ["apel", "mangga", "jeruk", "apel", "anggur", "mangga", "apel"]
# a) Cetak jumlah buah "apel" dalam list
# b) Buat list baru tanpa duplikat (unique list) dan urutkan abjad
# c) Ganti elemen pertama menjadi "buah_naga"
# TODO: Tulis kode Anda di bawah


# ============================================================================
# BAGIAN 3: KOMBINASI LOOP & LOGIKA KOMPLEKS
# ============================================================================

# Soal 5: Pola Segitiga Terbalik
# Buat pola segitiga terbalik dengan tinggi 5:
# *****
# ****
# ***
# **
# *
# TODO: Tulis kode Anda di bawah


# Soal 6: Bilangan Fibonacci Sederhana
# Cetak 10 angka pertama dari deret Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# Gunakan while loop
# TODO: Tulis kode Anda di bawah


# ============================================================================
# BAGIAN 4: KOMBINASI FUNGSI & DICTIONARY
# ============================================================================

# Soal 7: Data Mahasiswa dengan Fungsi
# Buat fungsi `tambah_mahasiswa(nama, jurusan)` yang menyimpan data di dictionary global
# dan fungsi `cari_mahasiswa(nama)` untuk mencari data
# Gunakan dictionary: mahasiswa = {}
# Contoh: tambah_mahasiswa("Budi", "Teknik Informatika")
#         cari_mahasiswa("Budi") -> "Jurusan: Teknik Informatika"
# TODO: Tulis kode Anda di bawah


# Soal 8: Fungsi Rekursif Sederhana
# Buat fungsi rekursif `faktorial(n)` yang menghitung faktorial dari n
# Contoh: faktorial(5) = 5 * 4 * 3 * 2 * 1 = 120
# TODO: Tulis kode Anda di bawah


# ============================================================================
# BAGIAN 5: MANIPULASI STRING & LIST KOMBINASI
# ============================================================================

# Soal 9: Analisis Kalimat
# Diberi string: "Python adalah bahasa pemrograman yang hebat dan powerful."
# a) Ubah menjadi list kata (split by space)
# b) Hitung berapa banyak kata yang panjangnya lebih dari 5 karakter
# c) Buat string baru hanya dari kata-kata yang panjangnya > 5 dan gabungkan dengan "-"
# TODO: Tulis kode Anda di bawah


# Soal 10: Palindrome Checker
# Buat fungsi `is_palindrome(kata)` yang mengembalikan True jika kata adalah palindrome
# Abaikan spasi dan huruf besar/kecil. Contoh: "Kasur ini rusak", "A man a plan a canal Panama"
# Untuk versi sederhana, cek: "level", "racecar", "hello"
# TODO: Tulis kode Anda di bawah


# ============================================================================
# BAGIAN 6: KOMBINASI SEMUA KONSEP - PROYEK MINI
# ============================================================================

# Soal 11: Manajemen Inventaris Sederhana
# Buat program inventaris barang menggunakan dictionary dan list.
# Struktur data: inventory = {"barang1": {"jumlah": 10, "harga": 5000}, ...}
# Buat fungsi:
# - tambah_barang(nama, jumlah, harga)
# - lihat_inventaris()
# - total_nilai_inventaris()
# - hapus_barang(nama)
# Gunakan fungsi-fungsi ini untuk menambah 3 barang, lalu tampilkan semua dan hitung total nilainya.
# TODO: Tulis kode Anda di bawah



# ============================================================================

"""
================================================================================
TANTANGAN TAMBAHAN (Opsional)
================================================================================
1. Buat fungsi `backup_data()` yang menyimpan data inventory ke dalam list tuples
   Format: [("nama_barang", jumlah, harga), ...]
2. Buat fungsi `restore_data(list_tuples)` untuk mengembalikan data ke inventory
================================================================================
"""

# TODO: Tulis kode Anda di bawah untuk tantangan tambahan
