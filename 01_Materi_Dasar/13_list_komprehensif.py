# LIST KOMPREHENSIF PYTHON
# List adalah tipe data array / kumpulan data yang berurutan dan isinya dapat diubah (mutable).

# 1. DEKLARASI LIST
print("==== 1. DEKLARASI & AKSES LIST ====")
data_list = [1, 5, 2, 7, 3]
data_campuran = [1, "Budi", 3.5, True]
print(f"Data list: {data_list}")
print(f"Data index ke-0: {data_list[0]}")
print(f"Data index terakhir (-1): {data_list[-1]}")

# 2. OPERASI DAN MANIPULASI LIST
print("\n==== 2. MANIPULASI LIST ====")
data_list.append(10) # Menambah elemen ke akhir list
print(f"Setelah append(10): {data_list}")

data_list.insert(2, 99) # Menambah elemen (99) pada index ke-2
print(f"Setelah insert(2, 99): {data_list}")

data_list.extend([11, 12]) # Menggabungkan dengan list lain
print(f"Setelah extend([11, 12]): {data_list}")

data_list.remove(99) # Menghapus elemen berdasarkan nilainya (angka 99)
print(f"Setelah remove(99): {data_list}")

data_pop = data_list.pop() # Menghapus elemen terakhir dan mengambil nilainya
print(f"Setelah pop() (yang terhapus: {data_pop}): {data_list}")

data_list.sort() # Mengurutkan data (Ascending)
print(f"Setelah sort(): {data_list}")
data_list.reverse() # Membalik urutan
print(f"Setelah reverse(): {data_list}")

# 3. LIST BERSARANG (NESTED LIST)
print("\n==== 3. NESTED LIST ====")
peserta1 = ["Budi", 25, "Pria"]
peserta2 = ["Siti", 22, "Wanita"]
peserta3 = ["Andi", 27, "Pria"]

list_peserta = [peserta1, peserta2, peserta3]
print(f"List Peserta: \n{list_peserta}")
# Mengakses elemen di nested list: [baris][kolom]
print(f"Nama peserta 2: {list_peserta[1][0]}")
print(f"Umur peserta 3: {list_peserta[2][1]}")

# 4. COPY LIST (Shallow Copy vs Deep Copy)
from copy import deepcopy
print("\n==== 4. COPY LIST ====")
data_asli = [1, 2, [3, 4]]
data_copy = data_asli.copy() # Shallow copy (Nested list tetap mereferensikan address yang sama)
data_deepcopy = deepcopy(data_asli) # Deep copy (Seluruh elemen termasuk nested di-copy)

data_asli[2][0] = 99
print(f"Data Asli (diubah sub-listnya): {data_asli}")
print(f"Shallow Copy (ikut berubah)   : {data_copy}")
print(f"Deep Copy (tetap aman)        : {data_deepcopy}")

# 5. LIST COMPREHENSION
# Cara singkat membuat list baru dari list yang sudah ada / range
print("\n==== 5. LIST COMPREHENSION ====")
list_angka = [1, 2, 3, 4, 5]
list_kuadrat = [i**2 for i in list_angka]
print(f"List kuadrat: {list_kuadrat}")

list_genap = [i for i in range(1, 11) if i % 2 == 0]
print(f"List Genap dari 1-10: {list_genap}")
