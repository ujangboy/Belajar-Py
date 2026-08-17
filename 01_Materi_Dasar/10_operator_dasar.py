# OPERATOR DASAR PYTHON

# 1. Operator Aritmatika
a = 10
b = 3
print("==== OPERATOR ARITMATIKA ====")
print(f"{a} + {b} = {a + b}")    # Penjumlahan
print(f"{a} - {b} = {a - b}")    # Pengurangan
print(f"{a} * {b} = {a * b}")    # Perkalian
print(f"{a} / {b} = {a / b}")    # Pembagian (hasil selalu float)
print(f"{a} // {b} = {a // b}")  # Pembagian bulat (Floor division)
print(f"{a} % {b} = {a % b}")    # Modulus (Sisa bagi)
print(f"{a} ** {b} = {a ** b}")  # Pangkat (Eksponen)

# 2. Operator Komparasi (Perbandingan) -> Output berupa Boolean
print("\n==== OPERATOR KOMPARASI ====")
x = 5
y = 10
print(f"{x} == {y} -> {x == y}")  # Sama dengan
print(f"{x} != {y} -> {x != y}")  # Tidak sama dengan
print(f"{x} > {y}  -> {x > y}")   # Lebih besar
print(f"{x} < {y}  -> {x < y}")   # Lebih kecil
print(f"{x} >= 5  -> {x >= 5}")   # Lebih besar sama dengan
print(f"{x} <= 5  -> {x <= 5}")   # Lebih kecil sama dengan

# 3. Operator Logika (untuk Boolean)
print("\n==== OPERATOR LOGIKA ====")
kondisi1 = True
kondisi2 = False
print(f"{kondisi1} AND {kondisi2} = {kondisi1 and kondisi2}") # Harus keduanya True
print(f"{kondisi1} OR {kondisi2}  = {kondisi1 or kondisi2}")  # Salah satu True = True
print(f"NOT {kondisi1}         = {not kondisi1}")             # Kebalikan

# 4. Operator Assignment (Penugasan)
print("\n==== OPERATOR ASSIGNMENT ====")
nilai = 5
print(f"Nilai awal = {nilai}")
nilai += 3  # sama dengan: nilai = nilai + 3
print(f"Setelah += 3, nilai menjadi {nilai}")
nilai -= 2  # sama dengan: nilai = nilai - 2
print(f"Setelah -= 2, nilai menjadi {nilai}")
nilai *= 4
print(f"Setelah *= 4, nilai menjadi {nilai}")
nilai /= 2
print(f"Setelah /= 2, nilai menjadi {nilai}")
nilai %= 3
print(f"Setelah %= 3, nilai menjadi {nilai}")

# 5. Operator Bitwise (Operasi biner tingkat rendah)
print("\n==== OPERATOR BITWISE ====")
c = 9   # Biner: 1001
d = 5   # Biner: 0101
print(f"{c} & {d} = {c & d}")   # Bitwise AND (0001 = 1)
print(f"{c} | {d} = {c | d}")   # Bitwise OR  (1101 = 13)
print(f"{c} ^ {d} = {c ^ d}")   # Bitwise XOR (1100 = 12)
print(f"~{c} = {~c}")           # Bitwise NOT
