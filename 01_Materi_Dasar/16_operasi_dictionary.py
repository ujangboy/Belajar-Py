# OPERASI DICTIONARY
# Bagaimana cara menambah, mengubah, dan menghapus elemen di dictionary.

data_dict = {
    "cup": "Cupucupu",
    "rey": "Reynaldi",
    "fik": "Fikri"
}
print("Data Awal:")
print(data_dict, "\n")

print("==== 1. MENAMBAH DAN MENGUBAH DATA ====")
# Cara 1: Langsung assignment dengan kurung siku
data_dict["cup"] = "Cupu-cupu" # Mengubah data (karena key 'cup' sudah ada)
data_dict["sep"] = "Asep"      # Menambah data (karena key 'sep' belum ada)
print("Setelah ubah & tambah pakai kurung siku:")
print(data_dict, "\n")

# Cara 2: Menggunakan .update() (Lebih disarankan)
# Jika key ada maka nilainya diubah, jika key tidak ada maka ditambah
data_dict.update({"rey": "Reynaldi Ganteng"}) # Mengubah
data_dict.update({"ujg": "Ujang Maman"})      # Menambah
print("Setelah menggunakan .update():")
print(data_dict, "\n")

print("==== 2. MENGHAPUS DATA ====")
# Cara 1: Menggunakan keyword 'del'
del data_dict["sep"]
print("Setelah del data_dict['sep']:")
print(data_dict, "\n")

# Cara 2: Menggunakan .pop()
# Sama seperti list, .pop() akan menghapus sekaligus me-return valuenya
data_dihapus = data_dict.pop("fik")
print(f"Data yang dihapus: {data_dihapus}")
print("Setelah pop('fik'):")
print(data_dict, "\n")

# Cara 3: Menggunakan .clear() untuk mengosongkan seluruh dictionary
# data_dict.clear() # Semua isi akan hilang
