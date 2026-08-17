# GENERATORS DAN ITERATORS

# 1. ITERATOR DASAR
print("==== 1. ITERATOR ====")

# Iterable adalah objek yang bisa di-loop (list, tuple, string, dict, set)
# Iterator adalah objek yang bisa menghasilkan nilai satu per satu dengan next()

angka_list = [1, 2, 3]
iter_obj = iter(angka_list)  # Buat iterator dari list

print(f"Next: {next(iter_obj)}")
print(f"Next: {next(iter_obj)}")
print(f"Next: {next(iter_obj)}")
# print(next(iter_obj))  # StopIteration error

# Manual loop sebenarnya memanggil next() secara otomatis
print("\nLoop manual dengan next():")
angka_list2 = [10, 20, 30]
it = iter(angka_list2)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

# 2. GENERATOR FUNCTION (YIELD)
print("\n==== 2. GENERATOR DENGAN YIELD ====")

def kuadrat_gen(n):
    for i in range(n):
        yield i ** 2  # yield mengembalikan nilai lalu jeda

gen = kuadrat_gen(5)
print(f"Tipe: {type(gen)}")
print("Hasil generator:")
for nilai in gen:
    print(nilai)

# Generator hanya mengeksekusi saat diminta (lazy evaluation)
def bilangan_genap(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i

print("\nBilangan genap < 10:")
for n in bilangan_genap(10):
    print(n)

# 3. GENERATOR EXPRESSION
print("\n==== 3. GENERATOR EXPRESSION ====")

# Mirip list comprehension tapi pakai () bukan []
list_comp = [x ** 2 for x in range(5)]
gen_exp = (x ** 2 for x in range(5))

print(f"List comprehension: {list_comp}")
print(f"Generator expression: {gen_exp}")  # Hanya alamat memori
print(f"List dari generator: {list(gen_exp)}")

# 4. KEUNTUNGAN GENERATOR (MEMORY EFFICIENT)
print("\n==== 4. MEMORY EFFICIENT ====")

import sys

# List vs Generator untuk data besar
data_list = list(range(1000000))
data_gen = (x for x in range(1000000))

print(f"Ukuran list: {sys.getsizeof(data_list)} bytes")
print(f"Ukuran generator: {sys.getsizeof(data_gen)} bytes")
print("Generator jauh lebih hemat memori!")

# 5. GENERATOR YG BISA DIKIRIM NILAI (SEND)
print("\n==== 5. GENERATOR DENGAN SEND ====")

def coroutine_gen():
    total = 0
    while True:
        nilai = yield total
        if nilai is not None:
            total += nilai

gen = coroutine_gen()
next(gen)  # Prime generator
print(f"Kirim 10: {gen.send(10)}")
print(f"Kirim 20: {gen.send(20)}")
print(f"Kirim 30: {gen.send(30)}")

# 6. ITERTOOLS (MODULE UNTUK ITERATOR)
print("\n==== 6. ITERTOOLS (Preview) ====")

import itertools

# count: infinite counter
counter = itertools.count(start=1, step=2)
print(f"Counter: {next(counter)}, {next(counter)}, {next(counter)}")

# islice: slice dari iterator
gen_angka = (x for x in range(20))
print(f"Slice 5 elemen: {list(itertools.islice(gen_angka, 5))}")

# chain: gabungkan multiple iterables
a = [1, 2, 3]
b = [4, 5, 6]
print(f"Chain: {list(itertools.chain(a, b))}")
