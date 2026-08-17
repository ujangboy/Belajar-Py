# DEKORATOR (DECORATOR)

# 1. FUNGSI SEBAGAI OBJEK PERTAMA
print("==== 1. FUNGSI SEBAGI OBJEK ====")

def sapa():
    print("Halo!")

def sebelum_sapa():
    print("=== Mulai ===")

# Kita bisa simpan fungsi di variabel
my_func = sapa
my_func()

# Fungsi bisa jadi parameter fungsi lain
def eksekusi(func):
    print("Menjalankan fungsi...")
    func()

eksekusi(sapa)

# 2. DEKORATOR SEDERHANA
print("\n==== 2. DEKORATOR SEDERHANA ====")

def DekoratorWaktu(func):
    def wrapper():
        import time
        mulai = time.time()
        func()
        selesai = time.time()
        print(f"Waktu eksekusi: {selesai - mulai:.4f} detik")
    return wrapper

def kerja_lama():
    import time
    time.sleep(0.5)
    print("Selesai bekerja!")

kerja_lama = DekoratorWaktu(kerja_lama)
kerja_lama()

# 3. SYNTAX @ (Syntactic Sugar)
print("\n==== 3. SYNTAX @ ====")

import time

def ukur_waktu(func):
    def wrapper(*args, **kwargs):
        mulai = time.time()
        hasil = func(*args, **kwargs)
        selesai = time.time()
        print(f"Waktu: {selesai - mulai:.4f} detik")
        return hasil
    return wrapper

@ukur_waktu
def hitung_faktorial(n):
    if n == 0 or n == 1:
        return 1
    return n * hitung_faktorial(n - 1)

print(f"5! = {hitung_faktorial(5)}")

# 4. DEKORATOR DENGAN ARGUMENT
print("\n==== 4. DEKORATOR DENGAN ARGUMENT ====")

def repeat(times):
    def dekorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"Eksekusi ke-{i + 1}:")
                func(*args, **kwargs)
        return wrapper
    return dekorator

@repeat(times=3)
def sapa_nama(nama):
    print(f"Halo, {nama}!")

sapa_nama("Budi")

# 5. FUNCTOOLS.WRAPS (MENJAGA METADATA FUNGSI)
print("\n==== 5. @functools.wraps ====")

from functools import wraps

def identificator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Memanggil: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@identificator
def tambah(a, b):
    return a + b

print(f"Hasil: {tambah(3, 4)}")
print(f"Nama fungsi asli: {tambah.__name__}")

# 6. DEKORATOR UNTUK CLASS
print("\n==== 6. DEKORATOR CLASS ====")

def tambah_method(cls):
    class Wrapper(cls):
        def salam(self):
            return f"Halo dari {self.__class__.__name__}"
    return Wrapper

@tambah_method
class Orang:
    def __init__(self, nama):
        self.nama = nama

o = Orang("Andi")
print(f"Nama: {o.nama}")
print(o.salam())
