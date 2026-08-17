# INPUT DAN OUTPUT DASAR

# 1. INPUT DARI USER
print("==== 1. INPUT DARI USER ====")
nama = input("Masukkan nama kamu: ")
print(f"Halo, {nama}!")

# Input selalu bertipe string, perlu casting jika mau angka
print("\n==== 2. CASTING INPUT ====")
angka_str = input("Masukkan angka: ")
angka = int(angka_str)  # Casting string ke integer
print(f"Angka yang kamu masukkan: {angka}, Bertipe: {type(angka)}")

# 3. FORMAT OUTPUT DENGAN f-string (paling disarankan)
print("\n==== 3. FORMAT OUTPUT ====")
nama = "Andi"
umur = 20
print(f"Nama: {nama}, Umur: {umur}")

# Format dengan separator ribuan dan 2 desimal
harga = 1000000.5
print(f"Harga: Rp {harga:,.2f}")

# Format rata kanan (align)
print(f"{'Nama':<10} {'Umur':<5}")
print(f"{nama:<10} {umur:<5}")

# 4. FORMAT DENGAN .format() (cara lama, masih sering dilihat di kode legacy)
print("\n==== 4. FORMAT LAMA (.format) ====")
print("Nama: {}, Umur: {}".format(nama, umur))
print("Nama: {0}, Umur: {1}".format(nama, umur))

# 5. PRINT DENGAN PARAMETER LANJUTAN
print("\n==== 5. PRINT LANJUTAN ====")
print("A", "B", "C", sep="-")           # Separator antar argumen
print("Ganti baris", end=" -> ")       # Mengubah akhir baris
print("Tetap di baris yang sama")

# 6. ESCAPE CHARACTER
print("\n==== 6. ESCAPE CHARACTER ====")
print("Baris 1\nBaris 2")           # \n = newline
print("Nama: \"Andi\"")             # \" = tanda kutip
print("Path: C:\\Users\\Andi")      # \\ = backslash literal
print('Bisa pakai kutip tunggal atau ganda fleksibel')
