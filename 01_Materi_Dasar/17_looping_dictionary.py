# LOOPING PADA DICTIONARY
# Bagaimana cara melakukan iterasi pada isi dictionary

teman_teman = {
    "cup": "Cupucupu",
    "rey": "Reynaldi",
    "fik": "Fikri",
    "sep": "Asep"
}

# Secara default, looping dictionary hanya mengambil Key-nya saja
print("==== DEFAULT LOOP (HANYA KEY) ====")
for t in teman_teman:
    print(t)

# 1. Iterasi Key (Sama dengan default, namun lebih eksplisit)
print("\n==== LOOPING KEY (.keys()) ====")
for k in teman_teman.keys():
    print(k)

# 2. Iterasi Value
print("\n==== LOOPING VALUE (.values()) ====")
for v in teman_teman.values():
    print(v)

# 3. Iterasi Key dan Value sekaligus
print("\n==== LOOPING KEY & VALUE (.items()) ====")
# items() akan mengembalikan Tuple (Key, Value) untuk tiap iterasi
for k, v in teman_teman.items():
    print(f"Kunci: {k} | Nilai: {v}")
