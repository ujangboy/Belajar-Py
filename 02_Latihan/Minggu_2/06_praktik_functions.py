"""
PRAKTIK PYTHON - SABTU (SATURDAY) - PRACTICE VERSION
Topik: Functions & Code Organization
Difficulty: Intermediate - Advanced

⚠️ INI ADALAH PRACTICE VERSION - TANPA SOLUSI
Coba kerjakan soal ini SEBELUM membuka Quiz Sabtu.py!
"""

print("=" * 60)
print("PRAKTIK SABTU - Functions & Code Organization")
print("=" * 60)
print()

# ============================================
# SOAL 1: Fungsi Luas Persegi Panjang
# ============================================
"""
TODO: Buat fungsi untuk menghitung luas persegi panjang
      
      - Function name: hitung_luas_persegi_panjang
      - Parameters: panjang, lebar
      - Return: luas
      - Test dengan panjang=10, lebar=5
      - Output: 50
"""

# TULIS KODE ANDA DI SINI:
def hitung_luas_persegi_panjang (panjang , lebar):
      luas = panjang * lebar
      return luas
luas = hitung_luas_persegi_panjang(10, 5)
print("Luas Persegi Panjang:", luas)      

# ============================================
# SOAL 2: Fungsi Cek Bilangan Prima
# ============================================
"""
TODO: Buat fungsi untuk mengecek bilangan prima
      
      - Function name: adalah_prima
      - Parameters: n
      - Return: True jika prima, False jika tidak
      - Test dengan n=17 (seharusnya True)
      - Test dengan n=20 (seharusnya False)
      
      Bilangan prima: hanya habis dibagi 1 dan dirinya sendiri
"""

# TULIS KODE ANDA DI SINI:
def adalah_prima(n):
      if n <= 1:
            return False
      for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                  return False
      return True
print("Apakah 17 bilangan prima?", adalah_prima(17))  # True
print("Apakah 20 bilangan prima?", adalah_prima(20))  # False

# ============================================
# SOAL 3: Fungsi Faktorial
# ============================================
"""
TODO: Buat fungsi untuk menghitung faktorial
      
      - Function name: hitung_faktorial
      - Parameters: n
      - Return: faktorial dari n
      - Test dengan n=5 (seharusnya 120)
      
      Faktorial 5 = 5 × 4 × 3 × 2 × 1 = 120
"""

# TULIS KODE ANDA DI SINI:
def hitung_faktorial(n):
      if n == 0 or n == 1:
            return 1
      else:
            return n * hitung_faktorial(n - 1)
print("Faktorial dari 5:", hitung_faktorial(5))  # 120      


# ============================================
# SOAL 4: Fungsi Konversi Suhu
# ============================================
"""
TODO: Buat fungsi untuk konversi suhu
      
      - Function name: konversi_suhu
      - Parameters: celsius, target (pilih "F", "K", atau "R")
      - Return: hasil konversi
      
      Rumus:
      - Celsius to Fahrenheit: (C × 9/5) + 32
      - Celsius to Kelvin: C + 273.15
      - Celsius to Reamur: C × 4/5
      
      Test dengan 25°C ke berbagai satuan
"""

# TULIS KODE ANDA DI SINI:
def konversi_suhu(celsius, target):
      if target == "F":
            return (celsius * 9/5) + 32
      elif target == "K":
            return celsius + 273.15
      elif target == "R":
            return celsius * 4/5
      else:
            return "Target konversi tidak valid"
      
print("25°C ke Fahrenheit:", konversi_suhu(25, "F"))  # 77.0
print("25°C ke Kelvin:", konversi_suhu(25, "K"))  # 298.15
print("25°C ke Reamur:", konversi_suhu(25, "R"))  # 20.0

# ============================================
# SOAL 5: Fungsi Sort List
# ============================================
"""
TODO: Buat fungsi yang mengurutkan list
      
      - Function name: sort_list
      - Parameters: list_input
      - Return: list terurut dari terkecil ke terbesar
      - Test dengan list = [45, 23, 67, 12, 89]
"""

# TULIS KODE ANDA DI SINI:
def sort_list(list_input):
      return sorted(list_input)
test_list = [45, 23, 67, 12, 89]
print("List sebelum diurutkan:", test_list)

# ============================================
# SOAL 6: Fungsi Hitung Rata-rata
# ============================================
"""
TODO: Buat fungsi untuk menghitung rata-rata
      
      - Function name: hitung_rata_rata
      - Parameters: list_nilai
      - Return: rata-rata nilai
      - Test dengan list = [85, 90, 78, 92, 88]
      - Output: 86.6
"""

# TULIS KODE ANDA DI SINI:
def hitung_rata_rata(list_nilai):
      total = sum(list_nilai)
      jumlah = len(list_nilai)
      return total / jumlah
nilai = [85, 90, 78, 92, 88]
print("Rata-rata nilai:", hitung_rata_rata(nilai))  # 86.6

# ============================================
# SOAL 7: Fungsi Validasi Password
# ============================================
"""
TODO: Buat fungsi untuk validasi password
      
      - Function name: validasi_password
      - Parameters: password
      - Return: True jika valid, False jika tidak
      
      Kriteria valid:
      - Minimal 8 karakter
      - Mengandung huruf besar
      - Mengandung huruf kecil
      - Mengandung angka
      
      Test: "Abc12345" → True, "password" → False
"""

# TULIS KODE ANDA DI SINI:


# ============================================
# SOAL 8: Fungsi Hitung Diskon
# ============================================
"""
TODO: Buat fungsi untuk menghitung diskon
      
      - Function name: hitung_diskon
      - Parameters: harga_asli, persentase_diskon
      - Return: tuple (diskon, harga_akhir)
      - Test dengan harga 100000 dan diskon 20%
      
      Output: (20000, 80000)
"""

# TULIS KODE ANDA DI SINI:


# ============================================
# SOAL 9: Fungsi Pangkat (Tanpa **)
# ============================================
"""
TODO: Buat fungsi untuk menghitung pangkat
      
      - Function name: hitung_pangkat
      - Parameters: base, exponent
      - Return: hasil pangkat
      - JANGAN gunakan operator ** atau pow()
      - Gunakan loop untuk mengalikan base
      - Test dengan 2^5 (seharusnya 32)
"""

# TULIS KODE ANDA DI SINI:


# ============================================
# SOAL 10: Fungsi dengan **kwargs
# ============================================
"""
TODO: Buat fungsi yang menerima **kwargs
      
      - Function name: buat_profil
      - Parameters: **kwargs (bisa nama, umur, email, kota, dll)
      - Return: string format profil
      
      Contoh penggunaan:
      buat_profil(nama="Andi", umur=25, email="andi@example.com")
      
      Output:
      Nama: Andi
      Umur: 25
      Email: andi@example.com
"""

# TULIS KODE ANDA DI SINI:


print()
print("=" * 60)
print("PRAKTIK SABTU SELESAI!")
print("Buka Quiz Sabtu.py untuk melihat solusi")
print("=" * 60)
