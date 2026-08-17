"""
PRAKTIK PYTHON - KAMIS (THURSDAY) - PRACTICE VERSION
Topik: Lists, Tuples & Operasi List
Difficulty: Intermediate

⚠️ INI ADALAH PRACTICE VERSION - TANPA SOLUSI
Coba kerjakan soal ini SEBELUM membuka Quiz Kamis.py!
"""

print("=" * 60)
print("PRAKTIK KAMIS - Lists, Tuples & Operasi List")
print("=" * 60)
print()

# ============================================
# SOAL 1: Hitung Rata-rata Nilai
# ============================================
"""
TODO: Buat list berisi 5 nilai matematika siswa
      Hitung rata-rata nilai tersebut
      nilai = [85, 90, 78, 92, 88]
      Output: Rata-rata = 86.6
      
      Hint: Gunakan sum() dan len()
"""

# TULIS KODE ANDA DI SINI:
nilai = [85, 90, 78, 92, 88]
rata_rata = sum(nilai) / len(nilai)
print(f"rata-rata = {rata_rata:.1f}")

# ============================================
# SOAL 2: Akses Elemen List dengan Index
# ============================================
"""
TODO: Diberikan list:
      buah = ["Apel", "Mangga", "Pisang", "Jeruk", "Pepaya"]
      
      Tampilkan:
      - Elemen pertama (index 0)
      - Elemen terakhir (index -1)
      - Elemen di index ke-2
"""

# TULIS KODE ANDA DI SINI:
buah = ["Apel", "Mangga", "Pisang", "Jeruk", "Pepaya"]
print(f"index buah: {buah.index('Apel')}")
print(f"elemen pertama: {buah[0]}")
print(f"elemen terakhir: {buah[-1]}")
print(f"elemen index ke-2: {buah[2]}")

# ============================================
# SOAL 3: List Slicing
# ============================================
"""
TODO: Gunakan list slicing untuk:
      angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
      
      a. Ambil 3 elemen pertama
      b. Ambil 3 elemen terakhir
      c. Ambil elemen dengan index ganjil
"""

# TULIS KODE ANDA DI SINI:
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f" 3 elemen perama: {angka[:3]}")
print(f" 3 elemen terakhir: {angka[-3:]}")
print(f" elemen dengan index ganjil: {angka[1::2]}")

# ============================================
# SOAL 4: Statistik List
# ============================================
"""
TODO: Diberikan list bilangan:
      bilangan = [45, 23, 67, 12, 89, 34, 56, 11, 98, 22]
      
      Hitung dan tampilkan:
      - Jumlah elemen (len())
      - Nilai minimum (min())
      - Nilai maksimum (max())
      - Jumlah total (sum())
"""

# TULIS KODE ANDA DI SINI:
bilangan = [45, 23, 67, 12, 89, 34, 56, 11, 98, 22]
print(f"jumlah elemen: {len(bilangan)}")
print(f"nilai minimal: {min(bilangan)}")
print(f"nilai maksimal: {max(bilangan)}")
print(f"jumlah total: {sum(bilangan)}")


# ============================================
# SOAL 5: Menggabungkan Dua List
# ============================================
"""
TODO: Gabungkan dua list menjadi satu
      list1 = [1, 2, 3]
      list2 = [4, 5, 6]
      Output: [1, 2, 3, 4, 5, 6]
      
      Hint: Gunakan operator + atau extend()
"""

# TULIS KODE ANDA DI SINI:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
gabungan = list1 + list2
print(f"gabungan list: {gabungan}")
# ============================================
# SOAL 6: Menghapus Elemen Duplikat
# ============================================
"""
TODO: Hapus elemen duplikat dalam list
      list_asli = [1, 2, 2, 3, 3, 3, 4, 5, 5]
      Output: [1, 2, 3, 4, 5] (terurut)
      
      Hint: Gunakan set() kemudian convert kembali ke list
"""

# TULIS KODE ANDA DI SINI:
lits_asli = [1, 2, 2, 3, 3, 3, 4, 5, 5]
list_unik = list(set(lits_asli))
list_unik.sort()
print(f"list unik: {list_unik}")

# ============================================
# SOAL 7: Operasi List Manipulation
# ============================================
"""
TODO: Lakukan operasi pada list:
      data = ["a", "b", "c", "d"]
      
      1. Tambahkan "e" ke akhir list (append)
      2. Masukkan "x" di posisi index 2 (insert)
      3. Hapus "b" dari list (remove)
      4. Tampilkan list setelah semua operasi
"""

# TULIS KODE ANDA DI SINI:
data = ["a", "b", "c", "d"]
data.append("e")
data.insert(2, "x")
data.remove("b")
print(f"list setelah operasi: {data}")

# ============================================
# SOAL 8: Sortir List
# ============================================
"""
TODO: Sort list dengan 2 cara
      nilai = [45, 23, 67, 12, 89, 34, 56]
      
      1. Tampilkan nilai terurut dari terkecil ke terbesar
      2. Tampilkan nilai terurut dari terbesar ke terkecil
      
      Hint: Gunakan sorted() dengan reverse=True
"""

# TULIS KODE ANDA DI SINI:
nilai = [45, 23, 67, 12, 12, 89, 34, 56]
nilai_axs = sorted(nilai)
nilai_axs_desc = sorted(nilai, reverse=True)
print(f"nilai terurut terkecil ke terbesar: {nilai_axs}")
print(f"nilai terurut terbesar ke terkecil: {nilai_axs_desc}")

# ============================================
# SOAL 9: Tuple dan Jarak Euclidean
# ============================================
"""
TODO: Hitung jarak antara 2 titik dalam 3D space
      Rumus: sqrt((x2-x1)² + (y2-y1)² + (z2-z1)²)
      
      titik1 = (1, 2, 3)
      titik2 = (4, 5, 6)
      
      Output: Jarak: 5.20
      
      Hint: Gunakan math.sqrt() atau **0.5
"""

# TULIS KODE ANDA DI SINI:
import math
titik1 = (1, 2, 3)
titik2 = (4, 5, 6)
jarak = math.sqrt((titik2[0]-titik1[0])**2 + (titik2[1]-titik1[1])**2 + (titik2[2]-titik1[2])**2)
print(f"jarak antara titik1 dan titik2: {jarak:.2f}")

# ============================================
# SOAL 10: Data Siswa - Berbagai Operasi
# ============================================
"""
TODO: Diberikan list nama siswa:
      siswa = ["Adi", "Budi", "Citra", "Dina", "Eka"]
      
      Buat program yang:
      a. Tampilkan nama siswa dengan nomor urut
      b. Cari posisi "Citra" dalam list
      c. Ganti nama "Budi" dengan "Budiman"
      d. Tampilkan jumlah total siswa
"""

# TULIS KODE ANDA DI SINI:
print("SOAL 10: Data Siswa")
siswa = ["Adi", "Budi", "Citra", "Dina", "Eka"]
print("a. Daftar siswa dengan nomor urut:")
for i, nama in enumerate(siswa, 1):
    print(f"   {i}. {nama}")

print(f"\nb. Posisi 'Citra': index {siswa.index('Citra')}")

siswa[1] = "Budiman"
print(f"\nc. Setelah ganti 'Budi' → 'Budiman': {siswa}")

print(f"\nd. Total siswa: {len(siswa)}")
print()

print()
print("=" * 60)
print("PRAKTIK KAMIS SELESAI!")
print("Buka Quiz Kamis.py untuk melihat solusi")
print("=" * 60)
