# OOP LANJUTAN (OBJECT ORIENTED PROGRAMMING)

# 1. CLASS DASAR (RECAP)
print("==== 1. RECAP CLASS DASAR ====")

class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        print(f"{self.nama} membuat suara.")

class Kucing(Hewan):
    def __init__(self, nama, warna):
        super().__init__(nama)
        self.warna = warna

    def suara(self):
        print(f"{self.nama} (kucing {self.warna}) mengongong.")

kucing1 = Kucing("Milo", "oren")
kucing1.suara()

# 2. ENCAPSULATION (PUBLIC, PROTECTED, PRIVATE)
print("\n==== 2. ENCAPSULATION ====")

class Rekening:
    def __init__(self, pemilik, saldo_awal):
        self.pemilik = pemilik          # Public
        self._saldo = saldo_awal        # Protected (_ satu underscore)
        self.__pin = "1234"             # Private (__ dua underscore, name mangling)

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, jumlah):
        if jumlah >= 0:
            self._saldo = jumlah
        else:
            print("Saldo tidak boleh negatif!")

    def get_pin(self):
        return self.__pin

rek = Rekening("Andi", 1000000)
print(f"Pemilik: {rek.pemilik}")
print(f"Saldo: {rek.get_saldo()}")
rek.set_saldo(1500000)
print(f"Saldo baru: {rek.get_saldo()}")
# print(rek.__pin)  # ERROR: AttributeError (private)

# 3. POLYMORPHISM (BANYAK BENTUK)
print("\n==== 3. POLYMORPHISM ====")

class Kucing:
    def bersuara(self):
        print("Kucing: Meong!")

class Anjing:
    def bersuara(self):
        print("Anjing: Guk guk!")

class Sapi:
    def bersuara(self):
        print("Sapi: Moo!")

def mainkan_hewan(hewan):
    hewan.bersuara()

mainkan_hewan(Kucing())
mainkan_hewan(Anjing())
mainkan_hewan(Sapi())

# 4. MAGIC METHODS (Dunder Methods)
print("\n==== 4. MAGIC METHODS ====")

class Buku:
    def __init__(self, judul, halaman):
        self.judul = judul
        self.halaman = halaman

    def __str__(self):
        return f"Buku '{self.judul}' ({self.halaman} halaman)"

    def __repr__(self):
        return f"Buku(judul='{self.judul}', halaman={self.halaman})"

    def __len__(self):
        return self.halaman

    def __add__(self, buku_lain):
        return Buku(f"{self.judul} & {buku_lain.judul}", self.halaman + buku_lain.halaman)

b1 = Buku("LOTR", 300)
b2 = Buku("Harry Potter", 400)

print(str(b1))        # __str__
print(repr(b1))       # __repr__
print(f"Jumlah halaman: {len(b1)}")  # __len__
print(f"Gabungan buku: {b1 + b2}")   # __add__

# 5. PROPERTY DECORATOR
print("\n==== 5. @property ====")

class Persegi:
    def __init__(self, sisi):
        self._sisi = sisi

    @property
    def sisi(self):
        return self._sisi

    @sisi.setter
    def sisi(self, nilai):
        if nilai > 0:
            self._sisi = nilai
        else:
            raise ValueError("Sisi harus positif!")

    @property
    def luas(self):
        return self._sisi ** 2

    @property
    def keliling(self):
        return self._sisi * 4

p = Persegi(5)
print(f"Sisi: {p.sisi}")
print(f"Luas: {p.luas}")
print(f"Keliling: {p.keliling}")
p.sisi = 10
print(f"Sisi baru: {p.sisi}, Luas baru: {p.luas}")

# 6. CLASSMETHOD DAN STATICMETHOD
print("\n==== 6. @classmethod & @staticmethod ====")

class Mahasiswa:
    jumlah = 0

    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        Mahasiswa.jumlah += 1

    @classmethod
    def from_string(cls, data_str):
        nama, nim = data_str.split("-")
        return cls(nama, nim)

    @staticmethod
    def is_valid_nim(nim):
        return len(nim) == 8

m1 = Mahasiswa("Andi", "12345678")
m2 = Mahasiswa.from_string("Budi-87654321")

print(f"Mahasiswa 1: {m1.nama}, NIM: {m1.nim}")
print(f"Mahasiswa 2: {m2.nama}, NIM: {m2.nim}")
print(f"Valid NIM 12345678? {Mahasiswa.is_valid_nim('12345678')}")
print(f"Total mahasiswa: {Mahasiswa.jumlah}")

# 7. ABSTRACT BASE CLASS (ABC)
print("\n==== 7. ABSTRACT BASE CLASS ====")

from abc import ABC, abstractmethod

class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        pass

    @abstractmethod
    def keliling(self):
        pass

class PersegiPanjang(Bentuk):
    def __init__(self, p, l):
        self.p = p
        self.l = l

    def luas(self):
        return self.p * self.l

    def keliling(self):
        return 2 * (self.p + self.l)

pp = PersegiPanjang(10, 5)
print(f"Luas PP: {pp.luas()}")
print(f"Keliling PP: {pp.keliling()}")

# bentuk = Bentuk()  # ERROR: Tidak bisa instantiate abstract class
