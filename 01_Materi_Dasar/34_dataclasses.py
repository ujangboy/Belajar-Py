# DATACLASSES

# 1. APA ITU DATACLASS?
print("==== 1. DATACLASS DASAR ====")
print("Dataclass adalah class khusus yang otomatis generate")
print("__init__, __repr__, __eq__, dll untuk menyimpan data.")

from dataclasses import dataclass, field, fields, asdict, replace

@dataclass
class Mahasiswa:
    nama: str
    umur: int
    jurusan: str
    ipk: float = 0.0  # Default value

m1 = Mahasiswa("Andi", 20, "Informatika", 3.5)
m2 = Mahasiswa("Budi", 22, "Sistem Informasi")

print(f"Mahasiswa 1: {m1}")
print(f"Mahasiswa 2: {m2}")
print(f"Equal? {m1 == m2}")

# 2. DEFAULT VALUES DAN FIELD
print("\n==== 2. DEFAULT VALUES DAN FIELD ====")

from dataclasses import field
from typing import List

@dataclass
class Siswa:
    nama: str
    umur: int
    nilai: List[int] = field(default_factory=list)  # Default mutable
    aktif: bool = True
    id: int = field(default=0, compare=False)  # Tidak dihitung saat __eq__

s1 = Siswa("Siti", 18)
s1.nilai = [80, 90, 85]
print(f"Siswa: {s1}")

# 3. POST INIT (PROSES SETELAH INIT)
print("\n==== 3. __post_init__ ====")

@dataclass
class Produk:
    nama: str
    harga: float
    jumlah: int
    total: float = field(init=False)  # Tidak di-parse dari parameter

    def __post_init__(self):
        self.total = self.harga * self.jumlah
        if self.total < 0:
            raise ValueError("Total tidak boleh negatif")

p1 = Produk("Laptop", 10000000, 2)
print(f"Produk: {p1.nama}, Total: Rp {p1.total:,}")

# 4. ASDICT DAN REPLACE
print("\n==== 4. ASDICT DAN REPLACE ====")

print(f"As dict: {asdict(m1)}")
m1_update = replace(m1, umur=21, ipk=3.8)
print(f"Updated: {m1_update}")

# 5. FIELD DENGAN METADATA
print("\n==== 5. METADATA FIELD ====")

@dataclass
class Karyawan:
    nama: str = field(metadata={"unit": "text"})
    gaji: float = field(metadata={"unit": "rupiah", "min": 0})
    departemen: str = "IT"

k = Karyawan("Dewi", 8000000, "HR")
for f in fields(k):
    print(f"  {f.name}: {f.metadata}")

# 6. INHERITANCE DENGAN DATACLASS
print("\n==== 6. INHERITANCE ====")

@dataclass
class Person:
    nama: str
    umur: int

@dataclass
class Employee(Person):
    id_karyawan: str
    gaji: float = 0.0

e = Employee("Rina", 28, "E001", 9000000)
print(f"Karyawan: {e}")

# 7. FROZEN DATACLASS (IMMUTABLE)
print("\n==== 7. FROZEN DATACLASS ====")

from dataclasses import FrozenInstanceError

@dataclass(frozen=True)
class Point:
    x: float
    y: float

pt = Point(3.0, 4.0)
print(f"Point: {pt}")
try:
    pt.x = 10.0  # ERROR: frozen
except FrozenInstanceError:
    print("Tidak bisa mengubah frozen dataclass.")

# 8. ORDERABLE
print("\n==== 8. ORDERABLE ====")

@dataclass(order=True)
class Score:
    nilai: float
    nama: str = "Unknown"

scores = [Score(85), Score(92), Score(78)]
print(f"Sorted: {sorted(scores)}")
print(f"Max: {max(scores)}")
