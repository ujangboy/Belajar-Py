"""
PRAKTIK PYTHON - SENIN (MONDAY) - PRACTICE VERSION
Topik: Variables, Data Types & Basic Operations
Difficulty: Beginner

⚠️ INI ADALAH PRACTICE VERSION - TANPA SOLUSI
Coba kerjakan soal ini SEBELUM membuka Quiz Senin.py!
"""

print("=" * 60)
print("PRAKTIK SENIN - Variables, Data Types & Operators")
print("=" * 60)
print()

# ============================================
# SOAL 1: Variables dan Type
# ============================================
"""
TODO: Buat 3 variable dengan tipe data berbeda (int, str, float)
      dan tampilkan tipe data masing-masing menggunakan type()
      
      Contoh output:
      Nama: John, Tipe: <class 'str'>
      Umur: 25, Tipe: <class 'int'>
      Tinggi: 170.5, Tipe: <class 'float'>
"""

# TULIS KODE ANDA DI SINI:
nama = "John"
umur = 25
tinggi = 170.5
print(f"nama: {nama}")
print(f"umur: {umur}")
print(f"tinggi: {tinggi}")    

# ============================================
# SOAL 2: Operasi Aritmatika
# ============================================
"""
TODO: Hitung luas persegi panjang dengan panjang=10 dan lebar=5
      Tampilkan hasilnya
"""

# TULIS KODE ANDA DI SINI:
panjang = 10
lebar = 5

luas = panjang * lebar 
print(f"luas persegi panjang: {luas}")

# ============================================
# SOAL 3: Konversi Tipe Data
# ============================================
"""
TODO: Konversi string "123" menjadi integer
      Tambahkan 77
      Tampilkan hasilnya
"""

# TULIS KODE ANDA DI SINI:
Konversi = "123"
hasil_konversi = int(Konversi) + 77
print(f"Hasil konversi dan penambahan 77: {hasil_konversi}")

# ============================================
# SOAL 4: String Concatenation
# ============================================
"""
TODO: Gabungkan 3 string: "Selamat", "datang", "di Python"
      menjadi satu kalimat yang rapi
"""

# TULIS KODE ANDA DI SINI:
kata1 = "Selamat"
kata2 = "datang"
kata3 = "di Python"
kalimat = f"{kata1} {kata2} {kata3}"
print(kalimat)


# ============================================
# SOAL 5: String Repetition
# ============================================
"""
TODO: Ulangi karakter "*" sebanyak 20 kali
      Tampilkan sebagai border
"""

# TULIS KODE ANDA DI SINI:
print("*" * 20)

# ============================================
# SOAL 6: Operasi Comparison
# ============================================
"""
TODO: Bandingkan nilai: apakah 100 > 50?
      Tampilkan hasil comparison (True/False)
"""

# TULIS KODE ANDA DI SINI:
perbandingan = 100 > 50
print(f"Apakah 100 > 50? {perbandingan}")

# ============================================
# SOAL 7: Operasi Modulo
# ============================================
"""
TODO: Cari sisa pembagian 17 dibagi 5
      Gunakan operator %
"""

# TULIS KODE ANDA DI SINI:
angka1 = 17
angka2 = 5
sisa_pembagian = angka1 % angka2
print(f"Sisa pembagian {angka1} dibagi {angka2} adalah: {sisa_pembagian}")

# ============================================
# SOAL 8: Input dan Operasi
# ============================================
"""
TODO: Jumlahkan dua angka: 15 dan 25
      Tampilkan hasilnya dengan format yang jelas
      
      Opsional: Bisa juga minta input dari user dengan input()
"""

# TULIS KODE ANDA DI SINI:
angka_a = 15
angka_b = 25
hasil_jumlah = angka_a + angka_b
print(f"Hasil penjumlahan {angka_a} + {angka_b} = {hasil_jumlah}")


# ============================================
# SOAL 9: Konversi Satuan
# ============================================
"""
TODO: Konversi 5 kilometer menjadi meter
      (1 km = 1000 m)
      Tampilkan: "5 km = 5000 meter"
"""

# TULIS KODE ANDA DI SINI:
konversi = 5 * 1000
print(f"5 km = {konversi} meter")


# ============================================
# SOAL 10: Total Belanja (Multi-item)
# ============================================
"""
TODO: Hitung total belanja:
      - 3 apel @ Rp5.000 = Rp15.000
      - 2 jeruk @ Rp3.000 = Rp6.000  
      - 1 mangga @ Rp7.000 = Rp7.000
      
      Tampilkan detail dan total akhir dengan format rapi
"""

# TULIS KODE ANDA DI SINI:
apel = 3 * 5000
jeruk = 2 * 3000
mangga = 1 * 7000
total_belanja = apel + jeruk + mangga
print("Detail Belanja:") 
print(f"  3 apel @ Rp5.000 = Rp{apel:,}")
print(f"  2 jeruk @ Rp3.000 = Rp{jeruk:,}")
print(f"  1 mangga @ Rp7.000 = Rp{mangga:,}")
print(f"Total Belanja: Rp{total_belanja:,}")

print()
print("=" * 60)
print("PRAKTIK SENIN SELESAI!")
print("Buka Quiz Senin.py untuk melihat solusi")
print("=" * 60)
