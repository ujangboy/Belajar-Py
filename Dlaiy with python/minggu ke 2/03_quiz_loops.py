"""
QUIZ PYTHON - RABU (WEDNESDAY)
Topik: Loops (for & while)
Difficulty: Beginner - Intermediate
"""

# ============================================
# SOAL 1: Tampilkan Angka 1-10
# ============================================

print("SOAL 1: Tampilkan Angka 1-10")
for i in range(1, 11):
    print(i, end=" ")
print("\n")

# ============================================
# SOAL 2: Hitung Jumlah Total Angka 1-100
# ============================================

print("SOAL 2: Hitung Jumlah Total Angka 1-100")
total = 0
for i in range(1, 101):
    total += i
print(f"Jumlah total: {total}")
print()

# ============================================
# SOAL 3: Tabel Perkalian Angka 5
# ============================================

print("SOAL 3: Tabel Perkalian Angka 5")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
print()

# ============================================
# SOAL 4: Pola Bintang Segitiga
# ============================================

print("SOAL 4: Pola Bintang Segitiga")
n = 5
for i in range(1, n + 1):
    print("*" * i)
print()

# ============================================
# SOAL 5: Tampilkan Bilangan Genap 1-20
# ============================================

print("SOAL 5: Tampilkan Bilangan Genap 1-20")
for i in range(2, 21, 2):
    print(i, end=" ")
print("\n")

# ============================================
# SOAL 6: Hitung Faktorial
# ============================================

print("SOAL 6: Hitung Faktorial")
n = 5
faktorial = 1
for i in range(1, n + 1):
    faktorial *= i
print(f"Faktorial {n} = {faktorial}")
print()

# ============================================
# SOAL 7: Iterasi List dengan Nomor Urut
# ============================================

print("SOAL 7: Iterasi List dengan Nomor Urut")
list_buah = ["Apel", "Mangga", "Pisang", "Jeruk", "Pepaya"]
for idx, buah in enumerate(list_buah, 1):
    print(f"{idx}. {buah}")
print()

# ============================================
# SOAL 8: Hitung Kemunculan Huruf 'a'
# ============================================

print("SOAL 8: Hitung Kemunculan Huruf 'a'")
kalimat = "python adalah bahasa pemrograman yang canggih"
jumlah_a = 0
for huruf in kalimat:
    if huruf == 'a':
        jumlah_a += 1
print(f"Kalimat: {kalimat}")
print(f"Jumlah huruf 'a': {jumlah_a}")
print()

# ============================================
# SOAL 9: Deret Fibonacci (10 Angka)
# ============================================

print("SOAL 9: Deret Fibonacci (10 Angka)")
a, b = 0, 1
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b
print("\n")

# ============================================
# SOAL 10: Input Berulang Sampai 'keluar'
# ============================================

print("SOAL 10: Input Berulang Sampai 'keluar'")
print("(Contoh dengan 3 input dummy)")
inputs = ["hello", "world", "keluar"]
for inp in inputs:
    if inp == "keluar":
        print("Program selesai")
        break
    else:
        print(f"Anda mengetik: {inp}")
print()

# ============================================
# BONUS: Pola Piramid Terbalik
# ============================================

print("BONUS: Pola Piramid Terbalik")
n = 5
for i in range(n, 0, -1):
    print("*" * i)
print()

print("=" * 50)
print("QUIZ RABU SELESAI!")
print("=" * 50)
