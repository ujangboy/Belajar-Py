# ERROR DAN EXCEPTION HANDLING

# 1. ERROR UMUM YANG SERING TERJADI
print("==== 1. CONTOH ERROR ====")

# SyntaxError - terjadi saat mengetik kode salah
# NameError - variabel belum didefinisikan
# TypeError - tipe data tidak sesuai
# ValueError - nilai tidak sesuai
# IndexError - indeks list di luar jangkauan
# KeyError - key dictionary tidak ditemukan
# ZeroDivisionError - pembagian dengan nol
# FileNotFoundError - file tidak ditemukan

# 2. TRY - EXCEPT
print("\n==== 2. TRY - EXCEPT ====")

try:
    angka = int(input("Masukkan angka: "))
    hasil = 10 / angka
    print(f"10 / {angka} = {hasil}")
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol!")
except ValueError:
    print("Error: Input harus berupa angka!")
except Exception as e:
    print(f"Error lain: {e}")

# 3. TRY - EXCEPT - ELSE - FINALLY
print("\n==== 3. TRY - EXCEPT - ELSE - FINALLY ====")

try:
    file = open("file_uji.txt", "r")
    isi = file.read()
except FileNotFoundError:
    print("File tidak ditemukan.")
else:
    print(f"Isi file berhasil dibaca (panjang: {len(isi)} karakter)")
    file.close()
finally:
    print("Blok ini selalu dijalankan (cleanup)")

# 4. RAISE (MEMBUAT ERROR SENDIRI)
print("\n==== 4. RAISE ====")

def cek_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak boleh negatif!")
    if umur < 17:
        print("Masih di bawah umur.")
    else:
        print("Sudah cukup umur.")

try:
    cek_umur(-5)
except ValueError as e:
    print(f"Error: {e}")

# 5. CUSTOM EXCEPTION CLASS
print("\n==== 5. CUSTOM EXCEPTION ====")

class PasswordTerlaluPendekError(Exception):
    def __init__(self, panjang):
        self.panjang = panjang
        super().__init__(f"Password terlalu pendek! Panjang: {panjang}")

def validasi_password(pw):
    if len(pw) < 6:
        raise PasswordTerlaluPendekError(len(pw))
    print("Password valid.")

try:
    validasi_password("abc")
except PasswordTerlaluPendekError as e:
    print(f"Error: {e}")

# 6. BEST PRACTICE: JANGAN BLANK EXCEPT
print("\n==== 6. BEST PRACTICE ====")

def bagi_aman(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Pembagi nol")
        return None
    except TypeError:
        print("Error: Tipe data harus angka")
        return None

print(f"10 / 2 = {bagi_aman(10, 2)}")
print(f"10 / 0 = {bagi_aman(10, 0)}")
print(f"10 / 'a' = {bagi_aman(10, 'a')}")
