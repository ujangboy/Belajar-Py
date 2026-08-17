# LAMBDA, MAP, FILTER, REDUCE

# 1. LAMBDA (ANONYMOUS FUNCTION)
print("==== 1. LAMBDA ====")

# Lambda adalah fungsi tanpa nama (1 baris)
# Syntax: lambda parameter: expression

kali_dua = lambda x: x * 2
print(f"Kali 2 dari 5: {kali_dua(5)}")

tambah = lambda a, b: a + b
print(f"10 + 15 = {tambah(10, 15)}")

# Lambda dengan default parameter
sapa = lambda nama, sapaan="Halo": f"{sapaan}, {nama}!"
print(sapa("Andi"))
print(sapa("Siti", "Hi"))

# Lambda dalam list (untuk sorting, filtering)
nilai = [80, 45, 90, 30, 75, 60]
print(f"Nilai asli: {nilai}")

# 2. MAP (TERAPAN FUNGSI KE SEMUA ELEMEN)
print("\n==== 2. MAP ====")

# Map menerapkan fungsi ke setiap elemen iterable
angka = [1, 2, 3, 4, 5]

kuadrat = list(map(lambda x: x ** 2, angka))
print(f"Kuadrat {angka} = {kuadrat}")

# Map dengan multiple iterables
a = [1, 2, 3]
b = [10, 20, 30]
jumlah = list(map(lambda x, y: x + y, a, b))
print(f"Jumlah {a} + {b} = {jumlah}")

# Map dengan fungsi built-in
nama = ["andi", "budi", "cici"]
upper_nama = list(map(str.upper, nama))
print(f"Upper: {upper_nama}")

# 3. FILTER (MENYARING ELEMEN)
print("\n==== 3. FILTER ====")

angka = [10, 15, 20, 25, 30, 35, 40]

# Filter angka genap
genap = list(filter(lambda x: x % 2 == 0, angka))
print(f"Genap dari {angka}: {genap}")

# Filter nilai >= 25
nilai = [80, 45, 90, 30, 75, 60]
lulus = list(filter(lambda x: x >= 60, nilai))
print(f"Nilai lulus: {lulus}")

# Filter string yang diawali 'a'
buah = ["apel", "jeruk", "anggur", "mangga", "alpukat")
awal_a = list(filter(lambda x: x.startswith("a"), buah))
print(f"Buah diawali 'a': {awal_a}")

# 4. REDUCE (MENGGABUNGKAN ELEMEN)
print("\n==== 4. REDUCE ====")

from functools import reduce

angka = [1, 2, 3, 4, 5]

# Menjumlahkan semua elemen
total = reduce(lambda x, y: x + y, angka)
print(f"Jumlah {angka} = {total}")

# Mencari nilai maksimum
nilai = [45, 89, 23, 67, 12, 90]
maks = reduce(lambda x, y: x if x > y else y, nilai)
print(f"Nilai maks {nilai} = {maks}")

# Menggabungkan string
kata = ["Python", "adalah", "bahasa", "asik"]
kalimat = reduce(lambda x, y: x + " " + y, kata)
print(f"Kalimat: {kalimat}")

# 5. KAPAN PAKAI?
print("\n==== 5. KAPAN PAKAI ====")
print("- Lambda: untuk fungsi sederhana 1 baris")
print("- Map: ubah semua elemen (list comprehensions sering lebih readable)")
print("- Filter:筛选 elemen yang memenuhi kondisi")
print("- Reduce: gabungkan elemen menjadi satu nilai (agregasi)")

# Alternatif list comprehension untuk map/filter:
angka = [1, 2, 3, 4, 5]
kuadrat_lc = [x ** 2 for x in angka]
print(f"Kuadrat via list comp: {kuadrat_lc}")

genap_lc = [x for x in angka if x % 2 == 0]
print(f"Genap via list comp: {genap_lc}")
