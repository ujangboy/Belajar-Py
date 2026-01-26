#Operasi List, Set, dan String

"""len() = mengihitung jumlah total elemen
max() = mengembalikan nilai terbesar dari sekumlupan data atau elemen
min() = mengembalikan nilai terkecil dari sekumpulan data atau elemen
count() = menghitung jumlah kemunculan elemen tertentu dalam list atau string
in() = memeriksa apakah elemen tertentu ada dalam list, set, atau string
not in() = memeriksa apakah elemen tertentu tidak ada dalam list, set, atau string
append() = menambahkan elemen baru di akhir list"""

# contoh lits 
buah = ["apel", "banana", "cherry"]
print(len(buah))         # Output: 3
print(max(buah))         # Output: cherry (berdasarkan urutan alfabet)
print(min(buah))         # Output: apel (berdasarkan urutan alfabet)
print(buah.count("banana"))  # Output: 1
print("apel" in buah)        # Output: True
print("mangga" not in buah)   # Output: True
buah.append("mangga")
print(buah)               # Output: ['apel', 'banana', 'cherry', '

# contoh set
angka = {1, 2, 3, 4, 5}
print(len(angka))         # Output: 5
print(max(angka))         # Output: 5
print(min(angka))         # Output: 1
print(angka.count(3))     # Output: 1
print(3 in angka)         # Output: True
print(6 not in angka)      # Output: True
angka.add(6)
print(angka)              # Output: {1, 2, 3, 4, 5, 6}

# contoh string
teks = "hello world"
print(len(teks))          # Output: 11
print(max(teks))          # Output: 'w' (berdasarkan urutan karakter ASCII)
print(min(teks))          # Output: ' ' (spasi, berdasarkan urutan karakter ASCII)
print(teks.count("o"))    # Output: 2
print("hello" in teks)     # Output: True
print("python" not in teks)  # Output: True
teks += "!"
print(teks)               # Output: 'hello world!'mangga']

# keterangan append()
"""
List
.append()
Karena list bisa ditambah elemen satu per satu di akhir
Set
.add()
Karena set tidak berurutan dan tidak boleh duplikat, jadi tidak bisa append
String
+=
Karena string immutable, tidak bisa langsung diubah, harus dibuat ulang
"""