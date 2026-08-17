# VARIABEL DAN TIPE DATA DASAR PYTHON

# 1. VARIABEL
# Variabel adalah tempat/wadah untuk menyimpan data.
# Di Python, kita tidak perlu mendeklarasikan tipe datanya secara eksplisit.
print("==== 1. VARIABEL ====")
nama = "Ujang"   # Variabel 'nama' menyimpan string
umur = 20        # Variabel 'umur' menyimpan integer
print("Nama :", nama)
print("Umur :", umur)

# Variabel dapat ditimpa (Re-assignment)
umur = 21
print("Umur sekarang:", umur)

# 2. TIPE DATA STANDAR
print("\n==== 2. TIPE DATA DASAR ====")
# a. Integer (Angka bulat)
data_integer = 100
print(f"Data: {data_integer}, Bertipe: {type(data_integer)}")

# b. Float (Angka dengan koma/desimal)
data_float = 3.14
print(f"Data: {data_float}, Bertipe: {type(data_float)}")

# c. String (Kumpulan karakter / teks)
data_string = "Belajar Python Dasar"
print(f"Data: {data_string}, Bertipe: {type(data_string)}")

# d. Boolean (True atau False)
data_bool = True
print(f"Data: {data_bool}, Bertipe: {type(data_bool)}")

# e. Complex (Bilangan kompleks/imajiner - jarang dipakai di web/standar, sering di matematika/sains)
data_complex = complex(5, 6) # 5 + 6j
print(f"Data: {data_complex}, Bertipe: {type(data_complex)}")
