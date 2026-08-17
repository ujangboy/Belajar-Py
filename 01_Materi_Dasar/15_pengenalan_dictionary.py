# PENGENALAN DICTIONARY
# Dictionary (dict) adalah struktur data array di Python yang menggunakan sistem pasangan Key dan Value.
# Berbeda dengan list yang menggunakan index berupa angka berurutan (0, 1, 2, ...), 
# dictionary menggunakan index (Key) yang bisa kita tentukan sendiri (bisa string, angka, dll).

print("==== DEKLARASI DICTIONARY ====")
# Syntax: { "key1": "value1", "key2": "value2" }
data_dict = {
    "nama": "Budi Santoso",
    "umur": 25,
    "pekerjaan": "Programmer",
    "is_active": True
}
print(f"Data Keseluruhan:\n{data_dict}\n")

print("==== MENGAKSES VALUE DARI DICTIONARY ====")
# Cara 1: Menggunakan kurung siku []
print(f"Nama : {data_dict['nama']}")
# Catatan: Jika key tidak ada, cara 1 akan menyebabkan error (KeyError)

# Cara 2: Menggunakan method .get() (Lebih aman)
print(f"Umur : {data_dict.get('umur')}")
print(f"Hobi : {data_dict.get('hobi')}") # Jika tidak ada, mengembalikan None
# Bisa juga diset nilai default jika key tidak ditemukan
print(f"Gaji : {data_dict.get('gaji', 'Gaji belum disetel')}")
