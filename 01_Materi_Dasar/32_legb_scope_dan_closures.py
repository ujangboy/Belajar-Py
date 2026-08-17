# LEGB SCOPE DAN CLOSURES

# 1. ATURAN LEGB (LOCAL, ENCLOSING, GLOBAL, BUILT-IN)
print("==== 1. ATURAN LEGB ====")

x = "global x"  # Global

def scope_demo():
    x = "local x"  # Local
    print(f"Dalam fungsi: {x}")

scope_demo()
print(f"Luar fungsi: {x}")

# Python mencari variabel dalam urutan:
# L = Local (di dalam fungsi)
# E = Enclosing (di fungsi yang membungkus)
# G = Global (di module/file)
# B = Built-in (print, len, dll - bawaan Python)

# 2. GLOBAL KEYWORD
print("\n==== 2. GLOBAL KEYWORD ====")

counter = 0

def increment():
    global counter  # Akses variabel global
    counter += 1
    print(f"Counter dalam fungsi: {counter}")

increment()
increment()
print(f"Counter luar: {counter}")

# 3. NONLOCAL KEYWORD (UNTUK NESTED FUNCTION)
print("\n==== 3. NONLOCAL ====")

def outer():
    x = 10

    def inner():
        nonlocal x  # Akses variabel dari fungsi enclosing
        x += 5
        print(f"x di inner: {x}")

    inner()
    print(f"x di outer: {x}")

outer()

# 4. CLOSURES
print("\n==== 4. CLOSURES ====")

def buat_penjumlahan(x):
    def penjumlah(y):
        return x + y  # x diingat dari scope enclosing
    return penjumlah

tambah_5 = buat_penjumlahan(5)
tambah_10 = buat_penjumlahan(10)

print(f"5 + 3 = {tambah_5(3)}")
print(f"10 + 3 = {tambah_10(3)}")

# Closure: fungsi yang "mengingat" variabel dari scope tempat ia dibuat

# Contoh lain: counter dengan closure
def buat_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c = buat_counter()
print(f"Counter 1: {c()}")
print(f"Counter 2: {c()}")
print(f"Counter 3: {c()}")

# 5. VARIABLE HIDING / SHADOWING
print("\n==== 5. VARIABLE SHADOWING ====")

angka = 100

def shadow_demo():
    angka = 50  # Ini variabel baru (local), tidak mengubah global
    print(f"Di dalam: {angka}")

shadow_demo()
print(f"Di luar: {angka}")

# 6. BUILT-IN NAMES
print("\n==== 6. BUILT-IN ====")

# print, len, str, int, float, list, dict, set, tuple
# range, sum, min, max, abs, round, open, type, isinstance
print(f"Built-in len: {len('python')}")
print(f"Built-in sum: {sum([1, 2, 3])}")
print(f"Built-in max: {max([5, 2, 8, 1])}")

# Jangan TIMPA nama built-in dengan variabel!
# Salah: len = [1, 2, 3]   # len() tidak bisa dipakai lagi

# 7. BEST PRACTICE
print("\n==== 7. BEST PRACTICE ====")
print("- Hindari variabel global sebanyak mungkin")
print("- Gunakan return value daripada global")
print("- Gunakan nonlocal hanya saat perlu")
print("- Jangan timpa nama built-in")
