# =====================================
# PYTHON QUIZ - SENIN (MONDAY)
# Topik: Variables, Data Types & Basic Operations
# =====================================

"""
QUIZ SENIN - 10 SOAL
Fokus: Variabel, Tipe Data, dan Operasi Dasar

Jawab setiap soal dengan menuliskan kode Python yang sesuai.
"""

# SOAL 1: Buat 3 variabel untuk data diri (nama, umur, hobi) dan tampilkan dengan format yang rapi
# TODO: Buatkan kode untuk menampilkan data diri dengan format yang bagus

# SOAL 2: Konversi suhu dari Celcius ke Fahrenheit. 
# Rumus: F = (C * 9/5) + 32
# Input: 25 derajat Celsius
# Output: berapa derajat Fahrenheit?

# SOAL 3: Hitung luas lingkaran dengan radius 7
# Rumus: Luas = π * r²
# (gunakan 3.14 untuk nilai pi)

# SOAL 4: String manipulation - Pisahkan teks "Saya-Sedang-Belajar-Python" 
# menjadi list kata-kata terpisah
# Kemudian gabungkan kembali dengan pemisah " | "

# SOAL 5: Buat program untuk menghitung total harga setelah diskon
# Harga barang: 50000
# Diskon: 20%
# Berapakah harga akhir?

# SOAL 6: Diberikan string "1234567890". 
# Ekstrak karakter index 2 hingga 5 (gunakan slicing)
# Berapa karakter yang diambil?

# SOAL 7: Buat list berisi 5 nama teman Anda.
# Tampilkan nama teman ke-3 (index ke-2)
# Tampilkan jumlah total teman dalam list

# SOAL 8: Diberikan dict dengan data produk:
# {"nama": "Laptop", "harga": 5000000, "stok": 10}
# Ambil dan tampilkan masing-masing value dari dictionary tersebut

# SOAL 9: String "programmingpython" - 
# Ubah menjadi huruf besar, huruf kecil, dan Title Case
# Tampilkan semua hasilnya

# SOAL 10: Buat kalkulator sederhana:
# Jumlahkan: 25 + 15
# Kurangkan: 25 - 15
# Kalikan: 25 * 15
# Bagikan: 25 / 15
# Tampilkan semua hasil operasi

# =====================================
# BONUS CHALLENGE:
# Hitung umur Anda dalam hari, jam, dan menit
# (Asumsi: Hari ini adalah 17 April 2026)
# Misal lahir tanggal 1 Januari 2010, berapa hari/jam/menit hingga sekarang?
# ===================================== 
"a  b\tc\nd".split()  # ["a", "b", "c", "d"]

tanggalold = "04-12-2025"
bagian2 = tanggalold.split("-")
tanggalNew = "/".join(bagian2)
print(tanggalNew)


dataBuah = "apel, mangga, pisang, jeruk"
buah = dataBuah.split(", ")
buahGabungan = "; ".join(buah)
gabungan2 = " - ".join(buah)
print(buah)
print(buahGabungan)
print(gabungan2)

daftar_buah = ['pisang', 'salak', 'durian']
hasil_join = ", ".join(daftar_buah)
print(hasil_join)