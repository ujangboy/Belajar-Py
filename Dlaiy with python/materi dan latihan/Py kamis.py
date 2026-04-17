#memberikan nilai untuk multipel variabel 

#srot adalah untuk mengurutkan elemen dalam lits atau array secara ascending atau descending
#sorted adalah fungsi yang mengembalikan list baru yang sudah diurutkan tanpa mengubah list asli

##contoh sort
anggota = ["Budi", "Andi", "Siti", "Citra"]
anggota.sort()
print(anggota)  # Output: ['Andi', 'Budi', 'Citra', 'Siti']
#jadi pada kode ini lits di urtutkan secara ascending atau dari A ke Z

angka = [42, 7, 19, 3, 85]
angka.sort()        
print(angka)  # Output: [3, 7, 19, 42, 85]
#jadi pada kode ini angka di urutkan secara ascending atau dari angka kecil ke besar

mahasiswa =[
    ("budi", 20, 85),
    ("siti", 22, 90),
    ("andi", 20, 50),
    ("nayla", 23, 95)
]
sorted_mahasiswa = sorted(mahasiswa, key=lambda x: (x[0], x[1], x[2]))
print(sorted_mahasiswa)
#jadi pada kode ini data di urutkan berdasarkan nama, umur, dan nilai secara ascending  

print (" ")
#sudy kasus
#Kamu sedang membuat program kecil untuk mengelola daftar game yang kamu mainkan. Setiap game memiliki:
"""Nama
Tahun rilis
Rating (skala 1-10)
Kamu ingin menampilkan daftar game terbaik dengan aturan:

Prioritas utama: rating tertinggi (descending → dari 10 ke 1)
Jika rating sama: urutkan berdasarkan tahun rilis terbaru dulu (descending → 2025 lebih dulu daripada 2020)
Jika tahun juga sama: urutkan berdasarkan nama secara alfabet (ascending)"""

games = [
    ("The Legend of Zelda", 2023, 9.5),
    ("Minecraft", 2011, 9.0),
    ("Drak souls", 2011, 9.5),
    ("Stardew Valley", 2016, 9.5),
    ("Caleste", 2018, 9.0),
    ("Elden Ring", 2022, 9.5)
]

hasil_sort = sorted (games, key=lambda x: (-x[2], -x[1], x[0]))
for game in hasil_sort:
    print(game)

print("=" * 60)
print("materi list, tuple, set, dictionary")
"""materi list, tuple, set, dictionary
"""
# lits Koleksi yang Dapat Diubah (Mutable)
"""List adalah koleksi data yang dapat diubah, terurut, dan memungkinkan duplikat. 
Elemen dapat ditambah, dihapus, atau diubah setelah list dibuat.
"""
print("lits")
buah = ["apel", "pisang", "mangga"]
buah.append("lemon")     # untuk menambahkan elemen
buah[0] = "nanas"        # untuk ubah elemen
buah.remove("pisang")    # untuk menghapus elemen
print(buah)

"""Kegunaan:

- Menyimpan daftar data yang sering berubah (nilai siswa, item belanja, daftar tugas)
- Ketika Anda perlu menambah/menghapus/mengubah data
- Cocok untuk: Daftar nilai, daftar nama, daftar barang belanja, antrian
"""

print("=" * 60)

# tuple Koleksi yang Tidak Dapat Diubah (Immutable)
print("tuple")
"""Penjelasan: Tuple mirip list, tetapi tidak bisa diubah setelah dibuat. 
Cocok untuk data yang harus tetap konstan."""

koordinat = (10, 20, 30, 70)
print(koordinat[0])       # output: 10 karna di hitung dari index 0 
# misal 
# koordinat[0] = 5        # ini akan error karna tidak bisa di ubah

x, y, z, b = koordinat       # unpacking 
print(x, y, z,)            # output: 10 20 30

"""Kegunaan:

- Menyimpan data yang tidak boleh berubah (koordinat GPS, tanggal lahir, ID tetap)
- Lebih cepat dan aman dari list
- Bisa digunakan sebagai key di dictionary
-Cocok untuk: Koordinat, tanggal, ID produk, data konfigurasi tetap"""

print("=" * 60)

print("set")
# set  Koleksi Unik Tanpa Urutan
"""Penjelasan: Set adalah koleksi yang tidak terurut, 
tidak memiliki duplikat, dan dapat diubah. Cocok untuk operasi matematika himpunan.
"""

angka = {1, 2, 3, 4, 5, 5, 5} # duplikat otomatis akan dihapus
print(angka)    # output {1, 2, 3, 4, 5}

set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a & set_b)        # irisan: 3
print(set_a | set_b)        # gabungan: {1, 2, 3, 4, 5}
print(set_a - set_b)        # selisih: {1, 2}

"""Kegunaan:

- Menghilangkan duplikat dari data
- Operasi himpunan (irisan, gabungan, selisih)
- Cek keanggotaan dengan cepat
- Cocok untuk: Daftar user unik, tag artikel, kategori produk, filter data"""

print("=" * 60)

print("dictionary")
# DICTIONARY - Pasangan Key-Value
"""Penjelasan: Dictionary menyimpan data dalam bentuk pasangan kunci-nilai. 
Akses data menggunakan key, bukan index."""

siswa = {
    "nama": "Budi",
    "umur": 20,
    "jurusan": "Informatika"
}
print(siswa["nama"])           # Output: Budi
siswa["nilai"] = 85            # Tambah key baru
print(siswa.get("alamat", "Tidak ada"))  # Output: Tidak ada