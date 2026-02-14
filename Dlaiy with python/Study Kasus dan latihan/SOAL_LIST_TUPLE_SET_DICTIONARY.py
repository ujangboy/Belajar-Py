"""
SOAL LATIHAN - LIST, TUPLE, SET, DICTIONARY
============================================
10 Soal untuk melatih logika dan fundamental Python
Tingkat kesulitan: Beginner - Intermediate

Instruksi:
- Baca soal dengan baik
- Tulis kode Anda di bawah setiap soal
- Jalankan dan test kode Anda
- Jangan lihat jawaban sampai Anda mencoba!
"""

# ============================================================================
# SOAL 1: LIST - Manipulasi Daftar Nilai
# ============================================================================
print("=" * 70)
print("SOAL 1: Manipulasi Daftar Nilai (LIST)")
print("=" * 70)
print("""
Diberikan daftar nilai siswa: [75, 85, 90, 70, 88, 92, 78]

Tugas:
a) Tambahkan nilai 95 ke akhir list
b) Ubah nilai 70 menjadi 80
c) Hapus nilai 75
d) Tampilkan nilai tertinggi dan terendah
e) Hitung rata-rata nilai

Tulis kode Anda di bawah ini:
""")

# Tulis kode Anda di sini
nilai = [75, 85, 90, 70, 88, 92, 78]


print("\n")

# ============================================================================
# SOAL 2: LIST - Filter dan Pencarian
# ============================================================================
print("=" * 70)
print("SOAL 2: Filter dan Pencarian (LIST)")
print("=" * 70)
print("""
Diberikan daftar nama: ["Andi", "Budi", "Citra", "Doni", "Eka", "Fitra"]

Tugas:
a) Cari nama yang dimulai dengan huruf 'D'
b) Buat list baru berisi nama dengan panjang > 4 karakter
c) Tampilkan nama di posisi ganjil (index 1, 3, 5)
d) Balik urutan list (reverse)

Tulis kode Anda di bawah ini:
""")

# Tulis kode Anda di sini
nama = ["Andi", "Budi", "Citra", "Doni", "Eka", "Fitra"]


print("\n")

# ============================================================================
# SOAL 3: TUPLE - Unpacking dan Operasi
# ============================================================================
print("=" * 70)
print("SOAL 3: Unpacking dan Operasi (TUPLE)")
print("=" * 70)
print("""
Diberikan tuple: (100, 200, 300, 400, 500)

Tugas:
a) Lakukan unpacking ke variabel a, b, c, d, e
b) Hitung jumlah semua elemen
c) Cari elemen terbesar dan terkecil
d) Buat tuple baru dengan elemen yang dikalikan 2
e) Cek apakah 300 ada di tuple

Tulis kode Anda di bawah ini:
""")

# Tulis kode Anda di sini
data = (100, 200, 300, 400, 500)


print("\n")

# ============================================================================
# SOAL 4: TUPLE - Koordinat dan Jarak
# ============================================================================
print("=" * 70)
print("SOAL 4: Koordinat dan Jarak (TUPLE)")
print("=" * 70)
print("""
Diberikan dua koordinat:
- Titik A: (0, 0)
- Titik B: (3, 4)

Tugas:
a) Unpacking kedua koordinat
b) Hitung jarak antara A dan B menggunakan rumus: √((x2-x1)² + (y2-y1)²)
c) Tampilkan hasil dengan 2 desimal

Hint: Gunakan math.sqrt() atau ** 0.5

Tulis kode Anda di bawah ini:
""")

# Tulis kode Anda di sini
titik_a = (0, 0)
titik_b = (3, 4)


print("\n")

# ============================================================================
# SOAL 5: SET - Operasi Himpunan
# ============================================================================
print("=" * 70)
print("SOAL 5: Operasi Himpunan (SET)")
print("=" * 70)
print("""
Diberikan dua set:
- Set A: {1, 2, 3, 4, 5}
- Set B: {4, 5, 6, 7, 8}

Tugas:
a) Cari irisan (intersection) A dan B
b) Cari gabungan (union) A dan B
c) Cari selisih A - B
d) Cari selisih B - A
e) Cek apakah A dan B memiliki elemen yang sama

Tulis kode Anda di bawah ini:
""")

# Tulis kode Anda di sini
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}


print("\n")

# ============================================================================
# SOAL 6: SET - Menghilangkan Duplikat
# ============================================================================
print("=" * 70)
print("SOAL 6: Menghilangkan Duplikat (SET)")
print("=" * 70)
print("""
Diberikan list dengan banyak duplikat:
[1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]

Tugas:
a) Ubah list menjadi set untuk menghilangkan duplikat
b) Hitung berapa banyak elemen unik
c) Ubah kembali ke list dan urutkan
d) Tampilkan elemen yang paling sering muncul di list asli

Tulis kode Anda di bawah ini:
""")

# Tulis kode Anda di sini
data_duplikat = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]


print("\n")

# ============================================================================
# SOAL 7: DICTIONARY - Data Produk
# ============================================================================
print("=" * 70)
print("SOAL 7: Data Produk (DICTIONARY)")
print("=" * 70)
print("""
Buat dictionary untuk menyimpan data produk:
- id: 101
- nama: "Laptop"
- harga: 8000000
- stok: 5
- kategori: "Elektronik"

Tugas:
a) Tampilkan semua informasi produk
b) Ubah harga menjadi 7500000
c) Tambahkan key baru "diskon" dengan nilai 10 (persen)
d) Hitung harga setelah diskon
e) Hapus key "kategori"

Tulis kode Anda di bawah ini:
""")

# Tulis kode Anda di sini
produk = {
    "id": 101,
    "nama": "Laptop",
    "harga": 8000000,
    "stok": 5,
    "kategori": "Elektronik"
}


print("\n")

# ============================================================================
# SOAL 8: DICTIONARY - Data Siswa Kompleks
# ============================================================================
print("=" * 70)
print("SOAL 8: Data Siswa Kompleks (DICTIONARY)")
print("=" * 70)
print("""
Buat dictionary untuk menyimpan data siswa dengan struktur kompleks:
{
    "nama": "Budi",
    "umur": 20,
    "nilai": {
        "matematika": 85,
        "bahasa_inggris": 90,
        "ipa": 88
    },
    "hobi": ["coding", "gaming", "membaca"]
}

Tugas:
a) Tampilkan nama siswa
b) Tampilkan nilai matematika
c) Tambahkan hobi baru "olahraga"
d) Hitung rata-rata nilai
e) Cek apakah "gaming" ada di hobi

Tulis kode Anda di bawah ini:
""")

# Tulis kode Anda di sini
siswa = {
    "nama": "Budi",
    "umur": 20,
    "nilai": {
        "matematika": 85,
        "bahasa_inggris": 90,
        "ipa": 88
    },
    "hobi": ["coding", "gaming", "membaca"]
}


print("\n")

# ============================================================================
# SOAL 9: KOMBINASI - Daftar Siswa dengan Dictionary dan List
# ============================================================================
print("=" * 70)
print("SOAL 9: Kombinasi - Daftar Siswa (LIST + DICTIONARY)")
print("=" * 70)
print("""
Buat list berisi dictionary untuk menyimpan data beberapa siswa:
[
    {"nama": "Andi", "nilai": 85, "kelas": "A"},
    {"nama": "Budi", "nilai": 90, "kelas": "B"},
    {"nama": "Citra", "nilai": 78, "kelas": "A"},
    {"nama": "Doni", "nilai": 92, "kelas": "B"}
]

Tugas:
a) Tampilkan nama semua siswa
b) Cari siswa dengan nilai tertinggi
c) Filter siswa dari kelas "A"
d) Hitung rata-rata nilai semua siswa
e) Tambahkan siswa baru: {"nama": "Eka", "nilai": 88, "kelas": "A"}

Tulis kode Anda di bawah ini:
""")

# Tulis kode Anda di sini
daftar_siswa = [
    {"nama": "Andi", "nilai": 85, "kelas": "A"},
    {"nama": "Budi", "nilai": 90, "kelas": "B"},
    {"nama": "Citra", "nilai": 78, "kelas": "A"},
    {"nama": "Doni", "nilai": 92, "kelas": "B"}
]


print("\n")

# ============================================================================
# SOAL 10: KOMBINASI - Analisis Data Hobi
# ============================================================================
print("=" * 70)
print("SOAL 10: Kombinasi - Analisis Data Hobi (SET + DICTIONARY + LIST)")
print("=" * 70)
print("""
Diberikan data hobi beberapa orang:
hobi_orang = {
    "Andi": {"coding", "gaming", "membaca"},
    "Budi": {"gaming", "olahraga", "membaca"},
    "Citra": {"coding", "menari", "membaca"},
    "Doni": {"olahraga", "gaming", "memasak"}
}

Tugas:
a) Cari hobi yang sama antara Andi dan Budi
b) Cari semua hobi unik dari semua orang
c) Cari hobi yang hanya dimiliki Andi
d) Cari orang yang memiliki hobi "gaming"
e) Hitung berapa banyak orang yang memiliki hobi "membaca"

Tulis kode Anda di bawah ini:
""")

# Tulis kode Anda di sini
hobi_orang = {
    "Andi": {"coding", "gaming", "membaca"},
    "Budi": {"gaming", "olahraga", "membaca"},
    "Citra": {"coding", "menari", "membaca"},
    "Doni": {"olahraga", "gaming", "memasak"}
}


print("\n" + "=" * 70)
print("SELESAI!")
print("=" * 70)
print("""
Tips:
- Jika stuck, coba breakdown soal menjadi bagian yang lebih kecil
- Gunakan print() untuk debug dan lihat hasilnya
- Coba berbagai cara untuk menyelesaikan soal
- Jangan takut untuk eksperimen!

Selamat belajar! 🚀
""")
