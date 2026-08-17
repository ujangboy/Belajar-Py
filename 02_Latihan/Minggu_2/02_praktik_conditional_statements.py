"""
PRAKTIK PYTHON - SELASA (TUESDAY) - PRACTICE VERSION
Topik: Conditional Statements (if/else/elif)
Difficulty: Beginner - Intermediate

⚠️ INI ADALAH PRACTICE VERSION - TANPA SOLUSI
Coba kerjakan soal ini SEBELUM membuka Quiz Selasa.py!
"""

print("=" * 60)
print("PRAKTIK SELASA - Conditional Statements")
print("=" * 60)
print()

# ============================================
# SOAL 1: Membandingkan Dua Bilangan
# ============================================
"""
TODO: Tentukan bilangan yang lebih besar di antara dua angka
      a = 45, b = 32
      Output: "45 lebih besar dari 32"
"""

# TULIS KODE ANDA DI SINI:
a = 45
b = 32
print(f"{a} lebih besar dari {b}" if a > b else f"{b} lebih besar dari {a}")

# ============================================
# SOAL 2: Sistem Penilaian Huruf
# ============================================
"""
TODO: Konversi nilai angka menjadi huruf grade
      Nilai >= 80: "A"
      Nilai >= 70: "B"
      Nilai >= 60: "C"
      Nilai < 60: "D"
      Test dengan nilai = 75
"""

# TULIS KODE ANDA DI SINI:
nilai = 75
if nilai >= 80:
    grade = "A"
elif nilai >= 70:
      grade = "B"
elif nilai >= 60:
      grade = "c"
else: 
      grade = "D"
      
print(f"Nilai {nilai} mendapatkan grade {grade}")
# ============================================
# SOAL 3: Cek Bilangan Genap atau Ganjil
# ============================================
"""
TODO: Tentukan apakah bilangan adalah genap atau ganjil
      Input: 27
      Output: "27 adalah bilangan ganjil"
      
      Hint: Gunakan operator %
"""

# TULIS KODE ANDA DI SINI:
angka = 27
if angka % 2 == 0:
      print(f"{angka} adalah bilangan genap")

# ============================================
# SOAL 4: Tentukan Musim Berdasarkan Bulan
# ============================================
"""
TODO: Tentukan musim berdasarkan bulan
      Januari-Maret: Musim Semi
      April-Juni: Musim Panas
      Juli-September: Musim Gugur
      Oktober-Desember: Musim Dingin
      Test dengan bulan = 7
"""

# TULIS KODE ANDA DI SINI:
bulan = 7
if 1 <= bulan <= 3:
      musim = "Musim Semi"
elif 4 <= bulan <= 6:
      musim = "Musim Panas"
elif 7 <= bulan <= 9:
      musim = "Musim Gugur"
else:
      musim = "Musim Dingin"
      
print(f"Bulan ke-{bulan} adalah {musim}")

# ============================================
# SOAL 5: Validasi Password
# ============================================
"""
TODO: Cek apakah password benar
      Password yang benar adalah "python123"
      Jika benar output: "Login berhasil"
      Jika salah output: "Password salah"
      Test dengan password = "python123"
"""

# TULIS KODE ANDA DI SINI:
password = "python123"
if password == "python123":
      print("Login berhasil")
else:      print("Password salah")

# ============================================
# SOAL 6: Tentukan Rating Film Berdasarkan Umur
# ============================================
"""
TODO: Tentukan rating film berdasarkan umur
      Umur < 13: "Hanya untuk anak di bawah 13 tahun"
      Umur 13-17: "PG-13"
      Umur >= 18: "Film dewasa"
      Test dengan umur = 16
"""

# TULIS KODE ANDA DI SINI:
print("rating film berdasarkan umur:")

umur = 16
if umur < 13:
      rating = "Hanya untuk anak di bawah 13 tahun"
elif 13 <= umur <= 17:
      rating = "PG-13"
else: rating = "Film dewasa"

print(f"Umur {umur} tahun: {rating}")

# ============================================
# SOAL 7: Cek Tahun Kabisat
# ============================================
"""
TODO: Cek apakah tahun adalah tahun kabisat
      Tahun kabisat jika: habis dibagi 4 
      AND (tidak habis dibagi 100 OR habis dibagi 400)
      
      Contoh:
      - 2024: kabisat (habis dibagi 4)
      - 2000: kabisat (habis dibagi 400)
      - 1900: bukan kabisat (habis 100 tapi tidak 400)
      
      Test dengan tahun = 2024
"""

# TULIS KODE ANDA DI SINI:
tahun = 2024
if (tahun % 4 == 0) and (tahun % 100 != 0 or tahun % 400 == 0):
      print(f"{tahun} adalah tahun kabisat")

# ============================================
# SOAL 8: Hitung Diskon Berdasarkan Total Belanja
# ============================================
"""
TODO: Hitung diskon berdasarkan total pembelian
      Pembelian <= 100000: Tanpa diskon (0%)
      Pembelian 100001-500000: Diskon 5%
      Pembelian 500001-1000000: Diskon 10%
      Pembelian > 1000000: Diskon 15%
      
      Test dengan total pembelian = 750000
      
      Output:
      Total Belanja: Rp750.000
      Diskon: 10% = Rp75.000
      Harga Akhir: Rp675.000
"""

# TULIS KODE ANDA DI SINI:
belanja = 750000
if belanja <= 100000:
      diskon = 0
elif 100001 <= belanja <= 500000:
      diskon = 0.05
elif 500001 <= belanja <= 1000000:
      diskon = 0.10
else:
      diskon = 0.15

diskon_rp = belanja * diskon
harga_akhir = belanja - diskon_rp
print(f"Total Belanja: Rp{belanja:,}")
print(f"Diskon: {int(diskon * 100)}% = Rp{diskon_rp:,}")
print(f"Harga Akhir: Rp{harga_akhir:,}")

# ============================================
# SOAL 9: Temukan Angka Terbesar dari 3 Angka
# ============================================
"""
TODO: Temukan angka terbesar dari 3 angka
      a = 10, b = 20, c = 30
      Output: "Angka terbesar adalah 30"
"""

# TULIS KODE ANDA DI SINI:
a = 10
b = 20
c = 30

if a >= b and a >= c:
      terbesar = a
elif b >= a and b >= c:
      terbesar = b
else:
      terbesar = c
print(f"Angka: {a}, {b}, {c}")
print(f"Angka terbesar adalah {terbesar}")

# ============================================
# SOAL 10: Validasi Email Sederhana
# ============================================
"""
TODO: Validasi email sederhana
      Email dianggap valid jika mengandung @ dan .
      Input: "emailcontohcom" (tanpa @)
      Output: "Email tidak valid"
      
      Input: "email@example.com"
      Output: "Email valid"
      
      Hint: Gunakan 'in' untuk cek karakter
"""

# TULIS KODE ANDA DI SINI:
valid_email = "email@example.com"
invalid_email = "emailcontohcom"    
email = invalid_email
if "@" in email and "." in email:
      print("Email valid")
else: print("Email tidak valid")



print()
print("=" * 60)
print("PRAKTIK SELASA SELESAI!")
print("Buka Quiz Selasa.py untuk melihat solusi")
print("=" * 60)
