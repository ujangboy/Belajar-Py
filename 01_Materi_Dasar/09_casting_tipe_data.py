# CASTING TIPE DATA
# Merubah tipe data dari satu tipe ke tipe yang lain
# Tipe data dasar: int, float, str, bool

print("==== INTEGER ====")
data_int = 9
print("data =", data_int, ", type =", type(data_int))

# Merubah int ke float, str, dan bool
data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int) # akan bernilai False jika nilai int = 0
print("data =", data_float, ", type =", type(data_float))
print("data =", data_str, ", type =", type(data_str))
print("data =", data_bool, ", type =", type(data_bool))

print("\n==== FLOAT ====")
data_float = 9.5
print("data =", data_float, ", type =", type(data_float))

# Merubah float ke int, str, dan bool
data_int  = int(data_float) # akan dibulatkan ke bawah (hilang koma)
data_str  = str(data_float)
data_bool = bool(data_float) # False jika 0.0
print("data =", data_int, ", type =", type(data_int))
print("data =", data_str, ", type =", type(data_str))
print("data =", data_bool, ", type =", type(data_bool))

print("\n==== BOOLEAN ====")
data_bool = True
print("data =", data_bool, ", type =", type(data_bool))

# Merubah bool ke int, float, dan str
data_int   = int(data_bool) # True = 1, False = 0
data_float = float(data_bool) # True = 1.0, False = 0.0
data_str   = str(data_bool) # Menjadi string "True" atau "False"
print("data =", data_int, ", type =", type(data_int))
print("data =", data_float, ", type =", type(data_float))
print("data =", data_str, ", type =", type(data_str))

print("\n==== STRING ====")
data_str = "10"
print("data =", data_str, ", type =", type(data_str))

# Merubah str ke int, float, dan bool
# Catatan: string harus berupa angka jika ingin diubah ke int atau float
data_int   = int(data_str) 
data_float = float(data_str)
data_bool  = bool(data_str) # False jika string kosong ""
print("data =", data_int, ", type =", type(data_int))
print("data =", data_float, ", type =", type(data_float))
print("data =", data_bool, ", type =", type(data_bool))
