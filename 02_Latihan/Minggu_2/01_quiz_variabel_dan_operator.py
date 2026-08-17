"""
QUIZ PYTHON - SENIN (MONDAY)
Topik: Variables, Data Types, dan Operators
Difficulty: Beginner
"""

# ============================================
# SOAL 1: Membuat dan mengelola variables
# ============================================
# Buat 3 variable dengan tipe data berbeda (int, str, float)
# dan tampilkan tipe data masing-masing menggunakan type()

# Solusi:
nama = "Uromastyx"
umur = 25
tinggi = 170.5
print("SOAL 1: Variables dan Type")
print(f"Nama: {nama}, Tipe: {type(nama)}")
print(f"Umur: {umur}, Tipe: {type(umur)}")
print(f"Tinggi: {tinggi}, Tipe: {type(tinggi)}")
print()

# ============================================
# SOAL 2: Operasi Aritmatika
# ============================================
# Hitung luas persegi panjang dengan panjang=10 dan lebar=5
# Tampilkan hasilnya

panjang = 10
lebar = 5
luas = panjang * lebar
print("SOAL 2: Operasi Aritmatika")
print(f"Panjang: {panjang}, Lebar: {lebar}")
print(f"Luas: {luas}")
print()

# ============================================
# SOAL 3: Konversi Tipe Data
# ============================================
# Konversi string "123" menjadi integer, tambahkan 77, tampilkan hasilnya

angka_string = "123"
angka_int = int(angka_string)
hasil = angka_int + 77
print("SOAL 3: Konversi Tipe Data")
print(f"String: {angka_string} → Integer: {angka_int} + 77 = {hasil}")
print()

# ============================================
# SOAL 4: Operasi String (Concatenation)
# ============================================
# Gabungkan 3 string: "Selamat", "datang", "di Python" menjadi satu kalimat

kata1 = "Selamat"
kata2 = "datang"
kata3 = "di Python"
kalimat = kata1 + " " + kata2 + " " + kata3
print("SOAL 4: String Concatenation")
print(kalimat)
print()

# ============================================
# SOAL 5: String Repetition
# ============================================
# Ulangi karakter "*" sebanyak 20 kali

simbol = "*" * 20
print("SOAL 5: String Repetition")
print(simbol)
print()

# ============================================
# SOAL 6: Operasi Comparison
# ============================================
# Bandingkan nilai: apakah 100 > 50? Tampilkan hasilnya

nilai1 = 100
nilai2 = 50
hasil = nilai1 > nilai2
print("SOAL 6: Operasi Comparison")
print(f"{nilai1} > {nilai2} = {hasil}")
print()

# ============================================
# SOAL 7: Operasi Modulo
# ============================================
# Cari sisa pembagian 17 dibagi 5

angka = 17
pembagi = 5
sisa = angka % pembagi
print("SOAL 7: Operasi Modulo")
print(f"{angka} mod {pembagi} = {sisa}")
print()

# ============================================
# SOAL 8: Input dari User dan Operasi
# ============================================
# Minta user input 2 angka, jumlahkan, dan tampilkan hasilnya
# (Uncomment untuk mencoba interaktif)

# print("SOAL 8: Input dan Operasi")
# angka_a = int(input("Masukkan angka pertama: "))
# angka_b = int(input("Masukkan angka kedua: "))
# jumlah = angka_a + angka_b
# print(f"Jumlah: {jumlah}")

# Contoh dengan nilai fixed:
angka_a = 15
angka_b = 25
jumlah = angka_a + angka_b
print("SOAL 8: Input dan Operasi")
print(f"Angka A: {angka_a}, Angka B: {angka_b}")
print(f"Jumlah: {jumlah}")
print()

# ============================================
# SOAL 9: Konversi Satuan
# ============================================
# Konversi 5 kilometer menjadi meter (1 km = 1000 m)

km = 5
meter = km * 1000
print("SOAL 9: Konversi Satuan")
print(f"{km} km = {meter} meter")
print()

# ============================================
# SOAL 10: Menghitung Total Belanja
# ============================================
# Hitung total belanja: 3 apel @Rp5000, 2 jeruk @Rp3000, 1 mangga @Rp7000

jumlah_apel = 3
harga_apel = 5000
jumlah_jeruk = 2
harga_jeruk = 3000
jumlah_mangga = 1
harga_mangga = 7000

total_apel = jumlah_apel * harga_apel
total_jeruk = jumlah_jeruk * harga_jeruk
total_mangga = jumlah_mangga * harga_mangga
total_belanja = total_apel + total_jeruk + total_mangga

print("SOAL 10: Total Belanja")
print(f"Apel: {jumlah_apel} x Rp{harga_apel:,} = Rp{total_apel:,}")
print(f"Jeruk: {jumlah_jeruk} x Rp{harga_jeruk:,} = Rp{total_jeruk:,}")
print(f"Mangga: {jumlah_mangga} x Rp{harga_mangga:,} = Rp{total_mangga:,}")
print(f"Total Belanja: Rp{total_belanja:,}")
print()

print("=" * 50)
print("QUIZ SENIN SELESAI!")
print("=" * 50)
