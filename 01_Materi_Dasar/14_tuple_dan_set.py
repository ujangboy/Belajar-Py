# TUPLE DAN SET DALAM PYTHON

# 1. TUPLE
# Tuple sama seperti List, memiliki indeks berurutan
# TETAPI isinya bersifat konstan / tidak bisa diubah (Immutable)
print("==== 1. TUPLE ====")
data_tuple = (1, 2, 3, 4, 5)
print(f"Data Tuple: {data_tuple}")
print(f"Data index ke-1: {data_tuple[1]}")

# Operasi yang dilarang di tuple:
# data_tuple[0] = 10 (TypeError: tuple object does not support item assignment)
# data_tuple.append(6) (AttributeError)

# Kapan menggunakan Tuple?
# Gunakan tuple untuk data-data statis yang tidak akan berubah bentuk / ukurannya.
# Tuple mengkonsumsi memori lebih sedikit dan proses iterasi sedikit lebih cepat dari List.

# 2. SET (HIMPUNAN)
# Set adalah koleksi data yang tidak berindeks dan tidak berurutan,
# serta tidak mengizinkan adanya nilai duplikat.
print("\n==== 2. SET (HIMPUNAN) ====")
data_set = {1, 2, 3, 3, 4, 4, 4, 5}
print(f"Data Set (Otomatis unik/tidak duplikat): {data_set}")

# Menambah & Menghapus data pada Set (Menggunakan fungsi bukan index)
data_set.add(6)
print(f"Setelah add(6): {data_set}")
data_set.remove(1)
print(f"Setelah remove(1): {data_set}")

# 3. OPERASI HIMPUNAN (MATEMATIKA SET)
print("\n==== 3. OPERASI HIMPUNAN ====")
himpunan_a = {1, 2, 3, 4, 5}
himpunan_b = {4, 5, 6, 7, 8}

print(f"Himpunan A: {himpunan_a}")
print(f"Himpunan B: {himpunan_b}")

# UNION (Gabungan dari himpunan A dan B)
print(f"A union B (A | B)       : {himpunan_a | himpunan_b}")

# INTERSECTION (Irisan - Elemen yang ada di A dan B)
print(f"A intersect B (A & B)   : {himpunan_a & himpunan_b}")

# DIFFERENCE (Selisih - Ada di A tapi tidak ada di B)
print(f"A difference B (A - B)  : {himpunan_a - himpunan_b}")

# SYMMETRIC DIFFERENCE (Hanya ada di A atau B, tidak keduanya)
print(f"A symmetric diff B (A ^ B): {himpunan_a ^ himpunan_b}")
