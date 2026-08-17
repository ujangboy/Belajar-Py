# ITERTOOLS (TOOLS UNTUK ITERATOR)

import itertools

# 1. INFINITE ITERATORS
print("==== 1. INFINITE ITERATORS ====")

# count(start, step) - infinite counter
counter = itertools.count(start=1, step=2)
print(f"Count 1-5: {list(itertools.islice(counter, 5))}")

# cycle(iterable) - loop forever
colors = itertools.cycle(["merah", "hijau", "biru"])
print(f"Cycle 5x: {list(itertools.islice(colors, 5))}")

# repeat(elem, times) - repeat elemen
repeated = itertools.repeat("halo", 3)
print(f"Repeat: {list(repeated)}")

# 2. ITERATOR YANG BERAKHIR
print("\n==== 2. ITERATOR BERAKHIR ====")

# accumulate(iterable, func) - akumulasi kumulatif
angka = [1, 2, 3, 4, 5]
akumulasi = list(itertools.accumulate(angka))
print(f"Kumulatif {angka} = {akumulasi}")

akumulasi_kali = list(itertools.accumulate(angka, lambda x, y: x * y))
print(f"Kumulatif kali = {akumulasi_kali}")

# chain(*iterables) - gabungkan multiple iterables
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8]
print(f"Chain: {list(itertools.chain(a, b, c))}")

# chain.from_iterable - chain dari iterable yang ada di dalam iterable
matrix = [[1, 2], [3, 4], [5, 6]]
print(f"Chain from iterable: {list(itertools.chain.from_iterable(matrix))}")

# compress(data, selectors) - filter dengan boolean selector
data = ["a", "b", "c", "d", "e"]
selector = [1, 0, 1, 0, 1]
print(f"Compress: {list(itertools.compress(data, selector))}")

# dropwhile(predicate, iterable) - skip selama predicate True
nums = [1, 2, 3, 4, 5, 1, 2]
print(f"Dropwhile < 4: {list(itertools.dropwhile(lambda x: x < 4, nums))}")

# takewhile(predicate, iterable) - ambil selama predicate True
print(f"Takewhile < 4: {list(itertools.takewhile(lambda x: x < 4, nums))}")

# filterfalse(predicate, iterable) - filter yang FALSE
genap = [2, 4, 6, 8, 10]
print(f"Filterfalse genap: {list(itertools.filterfalse(lambda x: x % 2 == 0, genap))}")

# islice(iterable, start, stop, step) - slice iterator
gen_angka = (x for x in range(20))
print(f"islice 0-5: {list(itertools.islice(gen_angka, 5))}")

# starmap(function, iterable) - map dengan unpacking
data_pair = [(1, 2), (3, 4), (5, 6)]
print(f"Starmap add: {list(itertools.starmap(lambda x, y: x + y, data_pair))}")

# tee(iterable, n) - clone iterator menjadi n buah iterator
it1, it2 = itertools.tee(range(5), 2)
print(f"Tee 1: {list(it1)}")
print(f"Tee 2: {list(it2)}")

# zip_longest(*iterables, fillvalue) - zip sampai yang terpanjang
a = [1, 2, 3]
b = ["a", "b"]
print(f"Zip longest: {list(itertools.zip_longest(a, b, fillvalue='?'))}")

# 3. KOMBINASI DAN PERMUTASI
print("\n==== 3. KOMBINASI DAN PERMUTASI ====")

buah = ["apel", "jeruk", "mangga"]

# combinations(iterable, r) - kombinasi tanpa urutan, tanpa pengulangan
print(f"Combinations 2: {list(itertools.combinations(buah, 2))}")

# combinations_with_replacement - dengan pengulangan
print(f"Combinations w/ replacement: {list(itertools.combinations_with_replacement(buah, 2))}")

# permutations(iterable, r) - permutasi dengan urutan
print(f"Permutations 2: {list(itertools.permutations(buah, 2))}")

# product(*iterables, repeat) - Cartesian product
warna = ["merah", "biru"]
print(f"Product warna x buah: {list(itertools.product(warna, buah))}")

# 4. GROUPBY
print("\n==== 4. GROUPBY ====")

data_group = [
    {"nama": "Andi", "jurusan": "IF"},
    {"nama": "Budi", "jurusan": "IF"},
    {"nama": "Cici", "jurusan": "TI"},
    {"nama": "Dewi", "jurusan": "TI"},
    {"nama": "Eko", "jurusan": "IF"},
]

# Group by jurusan (harus diurutkan terlebih dahulu!)
data_group.sort(key=lambda x: x["jurusan"])
for jurusan, group in itertools.groupby(data_group, key=lambda x: x["jurusan"]):
    anggota = list(group)
    print(f"  {jurusan}: {[d['nama'] for d in anggota]}")

# 5. BATCH / CHUNK
print("\n==== 5. CHUNK ====")

def batch(iterable, n):
    it = iter(iterable)
    while True:
        batch_data = list(itertools.islice(it, n))
        if not batch_data:
            break
        yield batch_data

print(f"Batch 3 dari [1..10]: {list(batch(range(1, 11), 3))}")

# 6. FLATTEN (RATAKAN NESTED LIST)
print("\n==== 6. FLATTEN ====")

nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat = list(itertools.chain.from_iterable(nested))
print(f"Flatten: {flat}")
