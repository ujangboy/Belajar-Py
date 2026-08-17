# COPY DICTIONARY
# Bagaimana cara menggandakan isi dictionary.

teman_teman = {
    "cup": "Cupucupu",
    "rey": "Reynaldi",
    "fik": "Fikri",
    "sep": "Asep"
}

print("==== 1. PERHATIAN (ASSIGNMENT BIASA) ====")
# Teman-teman dan friends akan merujuk pada alamat memori yang SAMA!
friends = teman_teman 

print(f"teman_teman : {teman_teman}")
print(f"friends     : {friends}")

teman_teman["cup"] = "Cupu Keren"
print("\nSetelah 'cup' di teman_teman diubah menjadi 'Cupu Keren':")
print(f"teman_teman : {teman_teman}")
print(f"friends     : {friends}") # Ikut berubah!

print("\n==== 2. COPY DICTIONARY (.copy()) ====")
# Untuk menggandakan ke memori yang baru, gunakan .copy()
teman_teman_asli = {
    "cup": "Cupucupu",
    "rey": "Reynaldi"
}

# Membuat copy yang terpisah dari variabel aslinya (Shallow copy)
kopi_teman = teman_teman_asli.copy()

kopi_teman["cup"] = "Cupu Tampan"

print(f"Teman asli  : {teman_teman_asli}")
print(f"Kopi teman  : {kopi_teman}") # Hanya kopi_teman yang berubah
