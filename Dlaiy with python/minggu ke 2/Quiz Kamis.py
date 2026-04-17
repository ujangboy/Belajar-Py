"""
QUIZ PYTHON - KAMIS (THURSDAY)
Topik: Lists, Tuples, dan Operasi List
Difficulty: Intermediate
"""

# ============================================
# SOAL 1: Hitung Rata-rata Nilai
# ============================================

print("SOAL 1: Hitung Rata-rata Nilai")
nilai = [85, 90, 78, 92, 88]
rata_rata = sum(nilai) / len(nilai)
print(f"Nilai: {nilai}")
print(f"Rata-rata: {rata_rata:.1f}")
print()

# ============================================
# SOAL 2: Akses Elemen List dengan Indexing
# ============================================

print("SOAL 2: Akses Elemen List")
buah = ["Apel", "Mangga", "Pisang", "Jeruk", "Pepaya"]
print(f"Elemen pertama (index 0): {buah[0]}")
print(f"Elemen terakhir (index -1): {buah[-1]}")
print(f"Elemen index ke-2: {buah[2]}")
print()

# ============================================
# SOAL 3: List Slicing
# ============================================

print("SOAL 3: List Slicing")
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"List asli: {angka}")
print(f"3 elemen pertama: {angka[:3]}")
print(f"3 elemen terakhir: {angka[-3:]}")
print(f"Elemen dengan index ganjil: {angka[1::2]}")
print()

# ============================================
# SOAL 4: Statistik List
# ============================================

print("SOAL 4: Statistik List")
bilangan = [45, 23, 67, 12, 89, 34, 56, 11, 98, 22]
print(f"List: {bilangan}")
print(f"Jumlah elemen: {len(bilangan)}")
print(f"Nilai minimum: {min(bilangan)}")
print(f"Nilai maksimum: {max(bilangan)}")
print(f"Jumlah total: {sum(bilangan)}")
print()

# ============================================
# SOAL 5: Menggabungkan Dua List
# ============================================

print("SOAL 5: Menggabungkan Dua List")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list_gabung = list1 + list2
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"List gabungan: {list_gabung}")
print()

# ============================================
# SOAL 6: Menghapus Elemen Duplikat
# ============================================

print("SOAL 6: Menghapus Elemen Duplikat")
list_asli = [1, 2, 2, 3, 3, 3, 4, 5, 5]
list_unik = list(set(list_asli))
list_unik.sort()
print(f"List asli: {list_asli}")
print(f"List tanpa duplikat: {list_unik}")
print()

# ============================================
# SOAL 7: Operasi List Manipulation
# ============================================

print("SOAL 7: Operasi List Manipulation")
data = ["a", "b", "c", "d"]
print(f"List awal: {data}")

data.append("e")  # Tambah di akhir
print(f"Setelah append('e'): {data}")

data.insert(2, "x")  # Masukkan di index 2
print(f"Setelah insert(2, 'x'): {data}")

data.remove("b")  # Hapus elemen 'b'
print(f"Setelah remove('b'): {data}")
print()

# ============================================
# SOAL 8: Sortir List
# ============================================

print("SOAL 8: Sortir List")
nilai = [45, 23, 67, 12, 89, 34, 56]
print(f"List asli: {nilai}")
print(f"Terurut kecil ke besar: {sorted(nilai)}")
print(f"Terurut besar ke kecil: {sorted(nilai, reverse=True)}")
print()

# ============================================
# SOAL 9: Tuple dan Jarak Euclidean
# ============================================

print("SOAL 9: Jarak Euclidean 3D")
import math

titik1 = (1, 2, 3)
titik2 = (4, 5, 6)

jarak = math.sqrt((titik2[0]-titik1[0])**2 + (titik2[1]-titik1[1])**2 + (titik2[2]-titik1[2])**2)
print(f"Titik 1: {titik1}")
print(f"Titik 2: {titik2}")
print(f"Jarak: {jarak:.2f}")
print()

# ============================================
# SOAL 10: Data Siswa - Berbagai Operasi
# ============================================

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

# ============================================
# BONUS: Rotasi List
# ============================================

print("BONUS: Rotasi List")
list_original = [1, 2, 3, 4, 5]
rotasi = 2
list_rotasi = list_original[-rotasi:] + list_original[:-rotasi]
print(f"List original: {list_original}")
print(f"Rotasi kanan {rotasi} kali: {list_rotasi}")
print()

print("=" * 50)
print("QUIZ KAMIS SELESAI!")
print("=" * 50)
