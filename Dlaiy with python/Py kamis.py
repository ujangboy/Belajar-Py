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