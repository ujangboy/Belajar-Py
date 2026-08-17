# FUNGSI DASAR DAN PARAMETER

# 1. DEFINISI FUNGSI DASAR
print("==== 1. FUNGSI DASAR ====")

def sapa():
    print("Halo dari fungsi!")

def sapa_nama(nama):
    print(f"Halo, {nama}!")

def tambah(a, b):
    return a + b

sapa()
sapa_nama("Budi")
hasil = tambah(10, 5)
print(f"10 + 5 = {hasil}")

# 2. PARAMETER DEFAULT
print("\n==== 2. PARAMETER DEFAULT ====")

def sapa_waktu(nama, waktu="pagi"):
    print(f"Selamat {waktu}, {nama}!")

sapa_waktu("Andi")
sapa_waktu("Siti", "siang")

# 3. PARAMETER BERDASARKAN NAMA (KEYWORD ARGUMENTS)
print("\n==== 3. KEYWORD ARGUMENTS ====")

def buat_profil(nama, umur, kota):
    print(f"Nama: {nama}, Umur: {umur}, Kota: {kota}")

buat_profil(umur=25, nama="Dewi", kota="Jakarta")

# 4. *ARGS (ARGUMENTS TIDAK BERBATAS)
print("\n==== 4. *ARGS ====")

def jumlahkan_semua(*angka):
    total = 0
    for n in angka:
        total += n
    return total

print(f"Jumlah 1,2,3 = {jumlahkan_semua(1, 2, 3)}")
print(f"Jumlah 1,2,3,4,5 = {jumlahkan_semua(1, 2, 3, 4, 5)}")

# 5. **KWARGS (KEYWORD ARGUMENTS TIDAK BERBATAS)
print("\n==== 5. **KWARGS ====")

def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(nama="Rina", umur=22, kota="Bandung")

# 6. KOMBINASI PARAMETER
print("\n==== 6. KOMBINASI PARAMETER ====")

def gabung(posisi, nama, *skills, **detail):
    print(f"Posisi: {posisi}")
    print(f"Nama: {nama}")
    print(f"Skills: {skills}")
    print(f"Detail: {detail}")

gabung("Backend", "Eko", "Python", "Django", "Flask", umur=28, kota="Surabaya")

# 7. RETURN VALUE
print("\n==== 7. RETURN VALUE ====")

def cek_genap(angka):
    if angka % 2 == 0:
        return True
    else:
        return False

print(f"4 genap? {cek_genap(4)}")
print(f"7 genap? {cek_genap(7)}")

# Return multiple values (packed sebagai tuple)
def operasi(a, b):
    return a + b, a - b, a * b

tambah, kurang, kali = operasi(8, 3)
print(f"8+3={tambah}, 8-3={kurang}, 8*3={kali}")

# 8. REKURSI (FUNGSI YANG MEMANGGIL DIRINYA SENDIRI)
print("\n==== 8. REKURSI ====")

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

print(f"5! = {faktorial(5)}")
print(f"3! = {faktorial(3)}")

# Rekursi sederhana: hitung mundur
def hitung_mundur(n):
    if n > 0:
        print(n)
        hitung_mundur(n - 1)

print("\nHitung mundur:")
hitung_mundur(5)
