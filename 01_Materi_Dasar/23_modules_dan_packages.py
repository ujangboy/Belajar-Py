# MODULES DAN PACKAGES

# 1. IMPORT STANDARD LIBRARY
print("==== 1. IMPORT MODULE ====")

import math

print(f"Pi: {math.pi}")
print(f"Akar 16: {math.sqrt(16)}")
print(f"Pembulatan 3.7: {math.ceil(3.7)}")
print(f"Pembulatan 3.7: {math.floor(3.7)}")

# Import dengan alias (nama lain)
import datetime as dt
sekarang = dt.datetime.now()
print(f"Sekarang: {sekarang}")

# Import spesifik fungsi
from random import randint, choice
print(f"Angka acak 1-10: {randint(1, 10)}")
print(f"Pilihan acak: {choice(['apel', 'jeruk', 'mangga'])}")

# Import semua (tidak disarankan karena bisa konflik nama)
from math import *
print(f"Sin 90: {sin(90)}")  # Tapi lebih baik pakai math.sin()

# 2. __name__ == "__main__"
print("\n==== 2. __name__ == '__main__' ====")
print("File ini dijalankan langsung, bukan di-import.")
print(f"__name__ = {__name__}")

# Jika file ini di-import oleh module lain, __name__ akan menjadi nama file
# Hanya print di atas yang muncul saat file dijalankan langsung

# 3. MEMBUAT MODULE SENDIRI
print("\n==== 3. MODULE SENDIRI ====")
# Contoh: buat file util.py dengan fungsi-fungsi, lalu import
# import util
# atau from util import nama_fungsi

# 4. PACKAGE (KOLEKSI MODULE)
print("\n==== 4. PACKAGE ====")
# Package adalah folder yang berisi __init__.py dan module-module
# Contoh struktur:
# mypackage/
#   __init__.py
#   math_ops.py
#   string_ops.py
#
# Import:
# from mypackage.math_ops import tambah
# import mypackage.string_ops as so

# 5. STANDARD LIBRARY YANG SERING DIPAKAI
print("\n==== 5. STANDARD LIBRARY ====")

import sys
print(f"Versi Python: {sys.version}")

import os
print(f"Current directory: {os.getcwd()}")

import json
data = {"nama": "Andi", "umur": 20}
json_str = json.dumps(data)
print(f"JSON string: {json_str}")

import re
pattern = r"\d+"
teks = "Ada 123 apel dan 456 jeruk"
angka = re.findall(pattern, teks)
print(f"Angka dalam teks: {angka}")

# 6. SYS.PATH (PENCARIAN MODULE)
print("\n==== 6. SYS.PATH ====")
print("Python mencari module di lokasi-lokasi berikut:")
for path in sys.path:
    print(f"  - {path}")
