"""
QUIZ PYTHON - SELASA (TUESDAY)
Topik: Conditional Statements (if/else/elif)
Difficulty: Beginner - Intermediate
"""

# ============================================
# SOAL 1: Membandingkan Dua Bilangan
# ============================================
# Tentukan bilangan yang lebih besar di antara dua angka

print("SOAL 1: Membandingkan Dua Bilangan")
a = 45
b = 32

if a > b:
    print(f"{a} lebih besar dari {b}")
elif b > a:
    print(f"{b} lebih besar dari {a}")
else:
    print(f"{a} sama dengan {b}")
print()

# ============================================
# SOAL 2: Sistem Penilaian Huruf
# ============================================
# Konversi nilai angka menjadi huruf grade

print("SOAL 2: Sistem Penilaian Huruf")
nilai = 75

if nilai >= 80:
    grade = "A"
elif nilai >= 70:
    grade = "B"
elif nilai >= 60:
    grade = "C"
else:
    grade = "D"

print(f"Nilai: {nilai} → Grade: {grade}")
print()

# ============================================
# SOAL 3: Cek Bilangan Genap atau Ganjil
# ============================================
# Tentukan apakah bilangan adalah genap atau ganjil

print("SOAL 3: Cek Bilangan Genap atau Ganjil")
angka = 27

if angka % 2 == 0:
    print(f"{angka} adalah bilangan genap")
else:
    print(f"{angka} adalah bilangan ganjil")
print()

# ============================================
# SOAL 4: Tentukan Musim Berdasarkan Bulan
# ============================================

print("SOAL 4: Tentukan Musim")
bulan = 7  # Juli

if 1 <= bulan <= 3:
    musim = "Musim Semi"
elif 4 <= bulan <= 6:
    musim = "Musim Panas"
elif 7 <= bulan <= 9:
    musim = "Musim Gugur"
else:
    musim = "Musim Dingin"

print(f"Bulan {bulan} → {musim}")
print()

# ============================================
# SOAL 5: Validasi Password
# ============================================

print("SOAL 5: Validasi Password")
password = "python123"
password_benar = "python123"

if password == password_benar:
    print("Login berhasil")
else:
    print("Password salah")
print()

# ============================================
# SOAL 6: Tentukan Rating Film Berdasarkan Umur
# ============================================

print("SOAL 6: Rating Film Berdasarkan Umur")
umur = 16

if umur < 13:
    rating = "Hanya untuk anak di bawah 13 tahun"
elif umur < 18:
    rating = "PG-13"
else:
    rating = "Film dewasa"

print(f"Umur: {umur} → {rating}")
print()

# ============================================
# SOAL 7: Cek Tahun Kabisat
# ============================================

print("SOAL 7: Cek Tahun Kabisat")
tahun = 2024

if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(f"{tahun} adalah tahun kabisat")
else:
    print(f"{tahun} bukan tahun kabisat")
print()

# ============================================
# SOAL 8: Hitung Diskon Berdasarkan Total Belanja
# ============================================

print("SOAL 8: Hitung Diskon Berdasarkan Total Belanja")
total_belanja = 750000

if total_belanja <= 100000:
    diskon_persen = 0
elif total_belanja <= 500000:
    diskon_persen = 5
elif total_belanja <= 1000000:
    diskon_persen = 10
else:
    diskon_persen = 15

diskon_nilai = total_belanja * diskon_persen / 100
harga_akhir = total_belanja - diskon_nilai

print(f"Total Belanja: Rp{total_belanja:,}")
print(f"Diskon: {diskon_persen}% = Rp{diskon_nilai:,.0f}")
print(f"Harga Akhir: Rp{harga_akhir:,.0f}")
print()

# ============================================
# SOAL 9: Temukan Angka Terbesar dari 3 Angka
# ============================================

print("SOAL 9: Temukan Angka Terbesar")
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
print()

# ============================================
# SOAL 10: Validasi Email Sederhana
# ============================================

print("SOAL 10: Validasi Email")
email = "emailcontohcom"

if "@" in email and "." in email:
    print("Email valid")
else:
    print("Email tidak valid")
print()

# ============================================
# BONUS: Hitung Jumlah Bilangan Genap & Ganjil
# ============================================

print("BONUS CHALLENGE: Hitung Genap & Ganjil")
angka_list = [12, 15, 24, 37, 42]
genap = 0
ganjil = 0

for num in angka_list:
    if num % 2 == 0:
        genap += 1
    else:
        ganjil += 1

print(f"Daftar angka: {angka_list}")
print(f"Jumlah bilangan genap: {genap}")
print(f"Jumlah bilangan ganjil: {ganjil}")
print()

print("=" * 50)
print("QUIZ SELASA SELESAI!")
print("=" * 50)
