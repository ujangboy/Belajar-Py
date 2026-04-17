"""
QUIZ PYTHON - JUMAT (FRIDAY)
Topik: Dictionaries dan String Operations
Difficulty: Intermediate
"""

# ============================================
# SOAL 1: Dictionary Data Profil
# ============================================

print("SOAL 1: Dictionary Data Profil")
profil = {
    "nama": "Andi Kurniawan",
    "email": "andi@example.com",
    "umur": 25,
    "kota": "Jakarta"
}
print("Profil Pengguna:")
for key, value in profil.items():
    print(f"  {key.capitalize()}: {value}")
print()

# ============================================
# SOAL 2: Dictionary Produk dan Harga
# ============================================

print("SOAL 2: Dictionary Produk dan Harga")
produk = {
    "Laptop": 5000000,
    "Mouse": 200000,
    "Keyboard": 350000,
    "Monitor": 1500000,
    "Headset": 400000
}
total_harga = sum(produk.values())
produk_termahal = max(produk, key=produk.get)

print("Daftar Produk:")
for nama, harga in produk.items():
    print(f"  {nama}: Rp{harga:,}")
print(f"\nTotal harga semua produk: Rp{total_harga:,}")
print(f"Produk termahal: {produk_termahal} (Rp{produk[produk_termahal]:,})")
print()

# ============================================
# SOAL 3: Modifikasi Dictionary
# ============================================

print("SOAL 3: Modifikasi Dictionary")
nilai_siswa = {"Adi": 85, "Budi": 90, "Citra": 78, "Dina": 92}
print(f"Dictionary awal: {nilai_siswa}")

nilai_siswa["Eka"] = 88  # Tambah siswa baru
print(f"Setelah tambah 'Eka': {nilai_siswa}")

nilai_siswa["Citra"] = 85  # Ubah nilai
print(f"Setelah ubah 'Citra': {nilai_siswa}")

del nilai_siswa["Budi"]  # Hapus data
print(f"Setelah hapus 'Budi': {nilai_siswa}")
print()

# ============================================
# SOAL 4: Iterasi Dictionary
# ============================================

print("SOAL 4: Iterasi Dictionary")
buku = {"Python": 2020, "JavaScript": 2019, "Java": 2018, "C++": 2017}
print("Daftar Buku dan Tahun Rilis:")
for bahasa, tahun in buku.items():
    print(f"  {bahasa}: {tahun}")
print()

# ============================================
# SOAL 5: Split dan Join String
# ============================================

print("SOAL 5: Split dan Join String")
teks = "Belajar-Python-Sangat-Menyenangkan"
print(f"Teks original: {teks}")

kata_kata = teks.split("-")
print(f"Setelah split('-'): {kata_kata}")

teks_gabung = " | ".join(kata_kata)
print(f"Setelah join(' | '): {teks_gabung}")
print()

# ============================================
# SOAL 6: Ekstrak Email
# ============================================

print("SOAL 6: Ekstrak Email")
email = "user@example.com"
print(f"Email: {email}")

bagian1 = email.split("@")
username = bagian1[0]
domain_full = bagian1[1]

bagian2 = domain_full.split(".")
domain = bagian2[0]
ekstensi = bagian2[1]

print(f"  Username: {username}")
print(f"  Domain: {domain}")
print(f"  Ekstensi: {ekstensi}")
print()

# ============================================
# SOAL 7: Format String (3 Cara)
# ============================================

print("SOAL 7: Format String")
nama = "Python"
versi = 3.9

# Cara 1: f-string
hasil1 = f"Bahasa {nama} versi {versi}"
print(f"f-string: {hasil1}")

# Cara 2: .format()
hasil2 = "Bahasa {} versi {}".format(nama, versi)
print(f".format(): {hasil2}")

# Cara 3: % operator
hasil3 = "Bahasa %s versi %.1f" % (nama, versi)
print(f"% operator: {hasil3}")
print()

# ============================================
# SOAL 8: String Methods
# ============================================

print("SOAL 8: String Methods")
teks = "  Python Programming Language  "
print(f"Teks original: '{teks}'")
print(f"strip(): '{teks.strip()}'")
print(f"upper(): '{teks.upper()}'")
print(f"lower(): '{teks.lower()}'")
print(f"replace('Python', 'JavaScript'): '{teks.replace('Python', 'JavaScript')}'")
print()

# ============================================
# SOAL 9: Dictionary Kontak Telepon
# ============================================

print("SOAL 9: Dictionary Kontak Telepon")
kontak = {"Adi": "082123456", "Budi": "081987654", "Citra": "083456789"}

print("a. Tambah kontak baru:")
kontak["Dina"] = "084111222"
print(f"   Kontak terbaru: {kontak}")

print("\nb. Cari nomor Citra:")
print(f"   {kontak.get('Citra', 'Tidak ditemukan')}")

print("\nc. Tampilkan semua kontak:")
for nama, nomor in kontak.items():
    print(f"   {nama}: {nomor}")
print()

# ============================================
# SOAL 10: Analisis String
# ============================================

print("SOAL 10: Analisis String")
kalimat = "Python adalah bahasa pemrograman yang fleksibel dan mudah dipelajari"
print(f"Kalimat: {kalimat}\n")

# Hitung kata
kata_list = kalimat.split()
jumlah_kata = len(kata_list)
print(f"a. Jumlah kata: {jumlah_kata}")

# Hitung huruf 'a'
jumlah_a = kalimat.count('a')
print(f"b. Jumlah huruf 'a': {jumlah_a}")

# Cari posisi kata
posisi = kalimat.find("fleksibel")
print(f"c. Posisi kata 'fleksibel': {posisi}")

# Balik urutan
kalimat_reverse = kalimat[::-1]
print(f"d. Kalimat terbalik (30 kar pertama): {kalimat_reverse[:30]}...")
print()

# ============================================
# BONUS: Konversi Format Tanggal
# ============================================

print("BONUS: Konversi Format Tanggal")
tanggal_str = "02-11-2025"
print(f"Tanggal original: {tanggal_str}")

# Pisahkan
bagian = tanggal_str.split("-")
hari = bagian[0]
bulan = int(bagian[1])
tahun = bagian[2]

# Format 1: DD/MM/YYYY
format1 = f"{hari}/{bulan_str}/{tahun}"
print(f"Format DD/MM/YYYY: {hari}/{bulan}/{tahun}")

# Format 2: DD Bulan YYYY
bulan_nama = {1: "Januari", 2: "Februari", 3: "Maret", 4: "April", 5: "Mei", 6: "Juni",
              7: "Juli", 8: "Agustus", 9: "September", 10: "Oktober", 11: "November", 12: "Desember"}
format2 = f"{hari} {bulan_nama[bulan]} {tahun}"
print(f"Format Deskriptif: {format2}")

# Format 3: YY-MM-DD
format3 = f"{tahun[-2:]}-{bagian[1]}-{hari}"
print(f"Format YY-MM-DD: {format3}")
print()

print("=" * 50)
print("QUIZ JUMAT SELESAI!")
print("=" * 50)
