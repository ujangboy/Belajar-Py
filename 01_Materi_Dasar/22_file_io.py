# FILE INPUT OUTPUT (FILE I/O)

# 1. MEMBACA FILE (READ)
print("==== 1. MEMBACA FILE ====")

# Menulis file dulu untuk contoh
with open("contoh.txt", "w") as f:
    f.write("Baris 1\nBaris 2\nBaris 3\n")

# Membaca seluruh isi file
with open("contoh.txt", "r") as f:
    isi = f.read()
    print("Isi file (read):")
    print(isi)

# Membaca per baris
print("Membaca per baris (readline):")
with open("contoh.txt", "r") as f:
    baris1 = f.readline()
    baris2 = f.readline()
    print(f"Baris 1: {baris1.strip()}")
    print(f"Baris 2: {baris2.strip()}")

# Membaca semua baris sebagai list
print("\nMembaca semua baris (readlines):")
with open("contoh.txt", "r") as f:
    semua_baris = f.readlines()
    for i, baris in enumerate(semua_baris, 1):
        print(f"Baris {i}: {baris.strip()}")

# 2. MENULIS FILE (WRITE)
print("\n==== 2. MENULIS FILE ====")

# Mode "w" = overwrite (hapus isi lama)
with open("catatan.txt", "w") as f:
    f.write("Ini catatan baru.\n")
    f.write("Baris kedua.\n")

# Mode "a" = append (tambah di akhir, jangan hapus yang lama)
with open("catatan.txt", "a") as f:
    f.write("Ini ditambahkan.\n")

print("Isi catatan.txt:")
with open("catatan.txt", "r") as f:
    print(f.read())

# 3. MODE FILE LAINNYA
print("\n==== 3. MODE FILE ====")
# "r" = read only (default)
# "w" = write only (overwrite, buat baru jika belum ada)
# "a" = append only
# "r+" = read + write (tidak overwrite, cursor di awal)
# "w+" = read + write (overwrite)
# "a+" = read + append

# 4. MENULIS DENGAN PRINT KE FILE
print("\n==== 4. PRINT KE FILE ====")

with open("output.txt", "w") as f:
    print("Ini dari print()", file=f)
    print("Baris kedua via print", file=f)

print("output.txt berhasil dibuat.")

# 5. MEMERIKSA KEBERADAAN FILE
print("\n==== 5. CEK FILE ====")

import os

if os.path.exists("contoh.txt"):
    print("File contoh.txt ADA")
    print(f"Ukuran: {os.path.getsize('contoh.txt')} bytes")
else:
    print("File contoh.txt TIDAK ADA")

# 6. MENGHAPUS FILE
# os.remove("file_lama.txt")

# 7. BINARY MODE (untuk gambar, pdf, dll)
print("\n==== 7. BINARY MODE ====")
with open("contoh.txt", "rb") as f:
    data_binary = f.read()
    print(f"Baca sebagai binary, panjang: {len(data_binary)} bytes")

# 8. WITH STATEMENT (PRAKTEK TERBAIK)
print("\n==== 8. WITH STATEMENT ====")
# with statement otomatis menutup file meskipun terjadi error
# Tidak perlu panggil f.close() secara manual
print("File otomatis ditutup setelah keluar dari blok with.")
