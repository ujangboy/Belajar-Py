"""
QUIZ PYTHON - SABTU (SATURDAY)
Topik: Functions dan Code Organization
Difficulty: Intermediate - Advanced
"""

# ============================================
# SOAL 1: Fungsi Luas Persegi Panjang
# ============================================

print("SOAL 1: Fungsi Luas Persegi Panjang")

def hitung_luas_persegi_panjang(panjang, lebar):
    """Menghitung luas persegi panjang"""
    return panjang * lebar

luas = hitung_luas_persegi_panjang(10, 5)
print(f"Luas persegi panjang (10 x 5): {luas} satuan²")
print()

# ============================================
# SOAL 2: Fungsi Cek Bilangan Prima
# ============================================

print("SOAL 2: Fungsi Cek Bilangan Prima")

def adalah_prima(n):
    """Mengecek apakah bilangan adalah prima"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"Apakah 17 prima? {adalah_prima(17)}")
print(f"Apakah 20 prima? {adalah_prima(20)}")
print()

# ============================================
# SOAL 3: Fungsi Faktorial
# ============================================

print("SOAL 3: Fungsi Faktorial")

def hitung_faktorial(n):
    """Menghitung faktorial dari n"""
    if n == 0 or n == 1:
        return 1
    hasil = 1
    for i in range(2, n + 1):
        hasil *= i
    return hasil

print(f"Faktorial 5: {hitung_faktorial(5)}")
print()

# ============================================
# SOAL 4: Fungsi Konversi Suhu
# ============================================

print("SOAL 4: Fungsi Konversi Suhu")

def konversi_suhu(celsius, target):
    """Konversi suhu ke berbagai satuan"""
    if target == "F":
        return (celsius * 9/5) + 32
    elif target == "K":
        return celsius + 273.15
    elif target == "R":
        return celsius * 4/5
    else:
        return None

print(f"25°C ke Fahrenheit: {konversi_suhu(25, 'F')}°F")
print(f"25°C ke Kelvin: {konversi_suhu(25, 'K')}K")
print(f"25°C ke Reamur: {konversi_suhu(25, 'R')}°R")
print()

# ============================================
# SOAL 5: Fungsi Sort List
# ============================================

print("SOAL 5: Fungsi Sort List")

def sort_list(list_input):
    """Mengurutkan list dari terkecil ke terbesar"""
    return sorted(list_input)

data = [45, 23, 67, 12, 89]
print(f"List original: {data}")
print(f"List terurut: {sort_list(data)}")
print()

# ============================================
# SOAL 6: Fungsi Hitung Rata-rata
# ============================================

print("SOAL 6: Fungsi Hitung Rata-rata")

def hitung_rata_rata(list_nilai):
    """Menghitung rata-rata nilai"""
    if len(list_nilai) == 0:
        return 0
    return sum(list_nilai) / len(list_nilai)

nilai = [85, 90, 78, 92, 88]
rata_rata = hitung_rata_rata(nilai)
print(f"Nilai: {nilai}")
print(f"Rata-rata: {rata_rata:.1f}")
print()

# ============================================
# SOAL 7: Fungsi Validasi Password
# ============================================

print("SOAL 7: Fungsi Validasi Password")

def validasi_password(password):
    """
    Validasi password dengan kriteria:
    - Minimal 8 karakter
    - Mengandung huruf besar
    - Mengandung huruf kecil
    - Mengandung angka
    """
    if len(password) < 8:
        return False
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    return has_upper and has_lower and has_digit

print(f"'Abc12345' valid? {validasi_password('Abc12345')}")
print(f"'password' valid? {validasi_password('password')}")
print()

# ============================================
# SOAL 8: Fungsi Hitung Diskon
# ============================================

print("SOAL 8: Fungsi Hitung Diskon")

def hitung_diskon(harga_asli, persentase_diskon):
    """Menghitung harga setelah diskon"""
    diskon = harga_asli * persentase_diskon / 100
    harga_akhir = harga_asli - diskon
    return (diskon, harga_akhir)

diskon, harga_akhir = hitung_diskon(100000, 20)
print(f"Harga asli: Rp100.000")
print(f"Diskon (20%): Rp{diskon:,.0f}")
print(f"Harga akhir: Rp{harga_akhir:,.0f}")
print()

# ============================================
# SOAL 9: Fungsi Pangkat (Tanpa **)
# ============================================

print("SOAL 9: Fungsi Pangkat (Tanpa **)")

def hitung_pangkat(base, exponent):
    """Menghitung pangkat tanpa operator **"""
    hasil = 1
    for _ in range(exponent):
        hasil *= base
    return hasil

print(f"2^5 = {hitung_pangkat(2, 5)}")
print()

# ============================================
# SOAL 10: Fungsi dengan **kwargs
# ============================================

print("SOAL 10: Fungsi dengan **kwargs")

def buat_profil(**kwargs):
    """Membuat profil orang dari berbagai parameter"""
    profil = ""
    for key, value in kwargs.items():
        profil += f"{key.capitalize()}: {value}\n"
    return profil

profil = buat_profil(nama="Andi", umur=25, email="andi@example.com", kota="Jakarta")
print("Profil Orang:")
print(profil)

# ============================================
# BONUS: Fungsi Fibonacci Rekursif
# ============================================

print("BONUS: Fungsi Fibonacci Rekursif")

def fibonacci(n):
    """Menghitung fibonacci secara rekursif"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(f"Fibonacci ke-10: {fibonacci(10)}")
print()

print("=" * 50)
print("QUIZ SABTU SELESAI!")
print("=" * 50)
