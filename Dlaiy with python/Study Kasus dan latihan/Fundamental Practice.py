"""
================================================================================
SOAL LATIHAN FUNDAMENTAL PYTHON
================================================================================
Latihan ini dirancang untuk melatih konsep dasar Python yang penting.
Selesaikan setiap soal dan gunakan print() untuk menampilkan hasil.
================================================================================
"""

# ============================================================================
# BAGIAN 1: VARIABEL & TIPE DATA
# ============================================================================

# Soal 1: Deklarasi Variabel
# Buat 3 variabel dengan tipe data berbeda (int, str, float)
# dan tampilkan tipenya menggunakan type()
# TODO: Tulis kode Anda di bawah
angga = 10
kata = "Halo Dunia"
desimal = 20.5
print(type(angga))
print(type(kata))
print(type(desimal))

# Soal 2: Operasi Aritmatika
# Diberi variabel a = 15, b = 4
# Hitung: penjumlahan, pengurangan, perkalian, pembagian (bulat), dan modulus
# TODO: Tulis kode Anda di bawah
a = 15
b = 4
print(a + b)          # penjumlahan
print(a - b)          # pengurangan
print(a * b)          # perkalian
print(a // b)         # pembagian (bulat)
print(a % b)          # modulus

# ============================================================================
# BAGIAN 2: STRING MANIPULATION
# ============================================================================

# Soal 3: Ubah Format String
# Diberikan string: "python adalah bahasa pemrograman"
# a) Ubah menjadi HURUF BESAR
# b) Ubah menjadi Huruf Pertama Besar di Setiap Kata
# c) Hitung berapa jumlah kata dalam string tersebut
# TODO: Tulis kode Anda di bawah
ubah = "python adalah bahasa pemrograman"
print(ubah.upper())                    # a) HURUF BESAR
print(ubah.title())                    # b) Huruf Pertama Besar di Setiap Kata
print(len(ubah.split()))               # c) Jumlah kata dalam string tersebut

# Soal 4: Pencarian dan Penggantian
# Diberikan string: "Saya suka makan apel, jeruk, dan pisang"
# a) Cari apakah kata "apel" ada dalam string
# b) Ganti "makan" dengan "membeli"
# c) Potong string dari karakter ke-5 sampai ke-15
# TODO: Tulis kode Anda di bawah
mencari = "Saya suka makan apel, jeruk, dan pisang"
print("apel" in mencari)                                   # a) Cari apakah kata "apel" ada dalam string
print(mencari.replace("makan", "membeli"))
print(mencari[4:15])                                      # c) Potong string dari karakter ke-5 sampai ke-15
"""Cara Kerja:
Index dimulai dari 0 (bukan 1):

S = index 0
a = index 1
y = index 2
a = index 3
  (spasi) = index 4
s = index 5
...dan seterusnya
Sintaks [4:15] berarti:

4 = mulai dari karakter di index 4
15 = berakhir SEBELUM index 15 (tidak termasuk index 15)
Jadi mengambil karakter dari index 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14

Index:  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16...
Char:   S a y a   s u k a   m  a  k  a  n     a...
                  ^                         ^
                  |_________  4:15  ________|
                  Dari sini      sampai sini (tidak termasuk)

"""

# Soal 5: Split dan Join
# Diberikan string: "jakarta,bandung,surabaya,medan"
# a) Pisahkan berdasarkan koma menggunakan split()
# b) Gabungkan kembali dengan separator " - " menggunakan join()
# TODO: Tulis kode Anda di bawah
kalimat = "jakarta,bandung,surabaya,medan"
print(kalimat.split(","))
print(" _ ".join(kalimat.split(",")))

# ============================================================================
# BAGIAN 3: LIST & INDEXING
# ============================================================================

# Soal 6: Operasi List Dasar
# Buat list berisi 5 nama buah: ["mangga", "apel", "pisang", "jeruk", "nanas"]
# a) Akses elemen pertama, ketiga, dan terakhir
# b) Ubah elemen kedua menjadi "papaya"
# c) Tambahkan "rambutan" di akhir list
# d) Hapus "jeruk" dari list
# TODO: Tulis kode Anda di bawah
nama_buah = ["mangga", "apel", "pisang", "jeruk", "nanas"]
print(f"a). emelen pertama: {nama_buah[0]}")           # a) elemen pertama
print(f"b). elemen ketiga: {nama_buah[2]}")        # a) elemen ketiga
print(f"b). elemen terakhir: {nama_buah[-1]}")       # a) elemen terakhir
nama_buah[1] = "papaya"    # b) Ubah elemen kedua menjadi "papaya"
nama_buah.append("rambutan") # c) Tambahkan "rambutan" di akhir list
nama_buah.remove("jeruk")   # d) Hapus "jeruk" dari list
print(nama_buah)
print(" ")

# Soal 7: Slicing List
# Diberikan list: numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# a) Ambil elemen dari index 2 sampai 5
# b) Ambil 4 elemen pertama
# c) Ambil 3 elemen terakhir
# d) Balikkan urutan list
# TODO: Tulis kode Anda di bawah
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(f"a) Ambil elemen dari index 2 sampai 5: {numbers[2:6]}")        # a) Ambil elemen dari index 2 sampai 5
print(f"b) Ambil 4 elemen pertama: {numbers[:4]}")                  # b) Ambil 4 elemen pertama
print(f"c) ambil 3 elemen terakhir: {numbers[-3:]}")               # c) Ambil 3 elemen terakhir
print(" ")
print("----------------------")

# Soal 8: List Comprehension
# Buat list berisi angka 1-10, kemudian buat list baru dengan
# menggunakan list comprehension:
# a) List berisi kuadrat dari setiap angka (1, 4, 9, 16, ...)
# b) List berisi hanya angka genap
# c) List berisi string dari setiap angka ("1", "2", "3", ...)
# TODO: Tulis kode Anda di bawah
list_angka = [1,2,3,4,5,6,7,8,9,10]
kuadrat = [a ** 2 for a in list_angka]        # a Kuadrat dari setiap angka
genap = [a for a in list_angka if a % 2 == 0] # b Hanya angka genap
string_angka = [str(a) for a in list_angka]   # c String dari setiap angka
print(f"a Kuadrat dari setiap angka: {kuadrat}")
print(f"b Hanya angka genap: {genap}")
print(f"c String dari setiap angka: {string_angka}")
print(" ")
print("----------------------------")

# ============================================================================
# BAGIAN 4: KONDISIONAL (IF-ELSE)
# ============================================================================

# Soal 9: Grade Siswa
# Diberi nilai (0-100), tentukan grade dengan ketentuan:
# 90-100: A, 80-89: B, 70-79: C, 60-69: D, <60: E
# Buat untuk nilai: 85, 75, 55
# TODO: Tulis kode Anda di bawah
nilai1 = 85
nilai2 = 75
nilai3 = 55
def tentukan_grade(nilai):
  if nilai >= 90:
    return "A"
  elif nilai >= 80:
    return "B"
  elif nilai >= 70:
    return "C"
  elif nilai >= 60:
    return "D"
  else:
    return "E"
print(f"Nilai: {nilai1}, Grade: {tentukan_grade(nilai1)}")
print(f"Nilai: {nilai2}, Grade: {tentukan_grade(nilai2)}")
print(f"Nilai: {nilai3}, Grade: {tentukan_grade(nilai3)}")
print(" ")
print("----------------------------")

# Soal 10: Cek Bilangan
# Buat program untuk cek apakah sebuah angka:
# a) Positif, negatif, atau nol
# b) Genap atau ganjil
# c) Prima atau bukan (gunakan angka: 7, 10, 13)
# TODO: Tulis kode Anda di bawah
def cek_bilangan(angka):
  # a) Positif, negatif, atau nol
  if angka > 0:
    status = "Positif"
  elif angka < 0:
    status = "Negatif"
  else:
    status = "Nol"
  
  # b) Genap atau ganjil
  if angka % 2 == 0:
    genap_ganjil = "Genap"
  else:
    genap_ganjil = "Ganjil"
  
  # c) Prima atau bukan
  if angka > 1:
    for i in range(2, int(angka**0.5) + 1):
      if angka % i == 0:
        prima = "Bukan Prima"
        break
    else:
      prima = "Prima"
  else:
    prima = "Bukan Prima"
  
  return status, genap_ganjil, prima
print(cek_bilangan(7))
print(cek_bilangan(10)) 
print(cek_bilangan(13))
print(" ")
print("----------------------------")
# ============================================================================
# BAGIAN 5: LOOP (FOR & WHILE)
# ============================================================================

# Soal 11: Loop dengan FOR
# a) Cetak angka 1-10 menggunakan for loop
# b) Cetak angka ganjil dari 1-20
# c) Cetak tabel perkalian 5 (5x1=5, 5x2=10, ... 5x10=50)
# TODO: Tulis kode Anda di bawah
print("a) Cetak angka 1-10")
for angka_loop in range(1, 11):
    print(angka_loop)                    # a) Cetak angka 1-10 menggunakan for loop
print("----------------------------")    
print("b) Cetak angka ganjil dari 1-20")
for angka_ganjil in range(1, 20):
    if angka_ganjil % 2 != 0:
      print(angka_ganjil)              # b) Cetak angka ganjil dari 1-20
print("----------------------------")
print("c) Cetak tabel perkalian 5")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")        # c) Cetak tabel perkalian 5   
    
print(" ")
print("----------------------------")
# Soal 12: Loop dengan WHILE
# a) Cetak angka dari 10 menurun ke 1
# b) Minta user input angka terus-menerus hingga user input "keluar"
# c) Hitung jumlah bilangan ganjil dari 1-50 menggunakan while loop
# TODO: Tulis kode Anda di bawah
print("a) Cetak angka dari 10 menurun ke 1:")
for i in range(10, 0, -1):
    print(i)                           # a) Cetak angka dari 10 menurun ke 1
print("----------------------------")
# b) Diblok karena akan menggunakan input (jalankan terpisah jika diperlukan)
"""
while True:
  user_input = input("b) Masukkan angka (ketik 'keluar' untuk berhenti): ")
  
  if user_input == "keluar":
    print("Program berhenti.")
    break
  
  print(f"Anda memasukkan angka: {user_input}")
"""
# c) Hitung jumlah bilangan ganjil dari 1-50 menggunakan while loop
print("c) Hitung jumlah bilangan ganjil dari 1-50:")
angka = 1
jumlah_ganjil = 0
while angka <= 50:
    if angka % 2 != 0:
        jumlah_ganjil += 1
    angka += 1
print(f"Total bilangan ganjil dari 1-50: {jumlah_ganjil}")
print("----------------------------")

# Soal 13: Nested Loop
# Buat segitiga angka dengan pola:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# TODO: Tulis kode Anda di bawah
print("Soal 13: Nested Loop - Segitiga Angka")
for baris in range(1, 6):
    for kolom in range(1, baris + 1):
      print(kolom, end=" ")
    print()  # Pindah ke baris berikutnya setelah selesai satu baris
print("----------------------------")
print(" ")
# ============================================================================
# BAGIAN 6: FUNGSI (FUNCTION)
# ============================================================================

# Soal 14: Fungsi Dasar
# Buat fungsi:
# a) sapa(nama) - return "Halo {nama}, selamat datang!"
# b) luas_persegi(sisi) - return luas persegi
# c) hitung_rata_rata(a, b, c) - return rata-rata 3 angka
# TODO: Tulis kode Anda di bawah
def sapa(nama):
    return f"Halo {nama}, selamat datang!"

print(sapa("Andi"))
print(sapa("Budi"))

def luas_persegi(sisi):
    return sisi * sisi 

print(f"Luas persegi dengan sisi 4: {luas_persegi(4)}")
print(f"Luas persegi dengan sisi 7: {luas_persegi(7)}")

def hitung_rata_rata(a, b, c):
    return (a + b + c) / 3

print(f"Rata-rata dari 5, 10, 15: {hitung_rata_rata(5, 10, 15)}")
print(" ")
print("----------------------------")
# Soal 15: Fungsi dengan Default Parameter
# Buat fungsi intro(nama, kota="Jakarta", pekerjaan="Engineer")
# Yang menampilkan: "Nama saya {nama}, saya dari {kota}, pekerjaan saya {pekerjaan}"
# Panggil dengan 1 argument, 2 arguments, dan 3 arguments
# TODO: Tulis kode Anda di bawah
def intro(nama, kota="Jakarta", pekerjaan="Engineer"):
    return f"Nama saya {nama}, saya dari {kota}, pekerjaan saya {pekerjaan}"

# Panggil dengan 1 argument
print(intro("Ali"))
# Output: Nama saya Ali, saya dari Jakarta, pekerjaan saya Engineer

# Panggil dengan 2 arguments (ganti kota)
print(intro("Budi", "Bandung"))
# Output: Nama saya Budi, saya dari Bandung, pekerjaan saya Engineer

# Panggil dengan 3 arguments
print(intro("Citra", "Surabaya", "Developer"))
# Output: Nama saya Citra, saya dari Surabaya, pekerjaan saya Developer

# Soal 16: Fungsi dengan *args (Multiple Arguments)
# Buat fungsi jumlahkan(*angka) yang menjumlahkan semua argument
# Test dengan jumlahkan(5), jumlahkan(5, 10), jumlahkan(1, 2, 3, 4, 5)
# TODO: Tulis kode Anda di bawah
def jumlahkan(*angka):
    """*angka = menerima BANYAK arguments"""
    total = 0
    for a in angka:
        total += a
    return total

# Test berbagai jumlah argument
print(jumlahkan(5))                    # Output: 5
print(jumlahkan(5, 10))                # Output: 15
print(jumlahkan(1, 2, 3, 4, 5))        # Output: 15

print(" ")
print("----------------------------")
# ============================================================================
# BAGIAN 7: DICTIONARY
# ============================================================================

# Soal 17: Dictionary Dasar
# Buat dictionary untuk data diri:
# {'nama': 'Budi', 'usia': 20, 'kota': 'Jakarta', 'hobi': 'programming'}
# a) Akses nilai dari key 'nama' dan 'hobi'
# b) Ubah nilai 'usia' menjadi 21
# c) Tambahkan key baru 'email': 'budi@gmail.com'
# d) Hapus key 'kota'
# TODO: Tulis kode Anda di bawah
data_diri = {'nama': 'Budi', 'usia': 20, 'kota': 'Jakarta', 'hobi': 'programming'}

print(f"a) Nama: {data_diri['nama']}, Hobi: {data_diri['hobi']}")  # a) Akses nilai dari key 'nama' dan 'hobi'
before = data_diri['usia']
print(f"b) Usia sebelum diubah: {before}")
data_diri['usia'] = 21
after = data_diri['usia']
print(f"   Usia setelah diubah: {after}")                            # b) Ubah nilai 'usia' menjadi 21
data_diri['email'] = 'budi12@gmail.com'
print(f"c) Tambah email: {data_diri['email']}")                     # c) Tambahkan key baru 'email': '
del data_diri['kota']
print(f"d) Hapus kota, sisa data: {data_diri}")                     # d) Hapus key 'kota'
print(" ")
print("----------------------------")

# Soal 18: Loop Dictionary
# Diberikan dictionary:
# siswa = {'Budi': 85, 'Ani': 92, 'Citra': 78, 'Doni': 88}
# a) Cetak semua nama siswa
# b) Cetak semua nilai
# c) Cetak nama dan nilai dalam format: "Budi mendapat nilai 85"
# d) Cari siswa dengan nilai tertinggi
# TODO: Tulis kode Anda di bawah
siswa = {'Budi': 85, 'Ani': 92, 'Citra': 78, 'Doni': 88}

for nama in siswa:
    print(nama)
for nilai in siswa.values():
    print(nilai)
for nama, nilai in siswa.items():
    print(f"{nama} mendapat nilai {nilai}")
tertinggi = max(siswa, key=siswa.get)
print(f"Siswa dengan nilai tertinggi: {tertinggi} dengan nilai {siswa[tertinggi]}")
print(" ")
print("----------------------------")

# Soal 19: Merge Dictionary
# Diberikan dua dictionary:
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# Gabungkan keduanya menjadi dict3 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# TODO: Tulis kode Anda di bawah
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Cara 1: Menggunakan update()
dict3 = dict1.copy()  # Buat salinan dict1
dict3.update(dict2)   # Gabungkan dict2 ke dict3
print(f"Cara 1 - Menggunakan update(): {dict3}")
# Cara 2: Menggunakan unpacking (Python 3.5+)
dict3_unpack = {**dict1, **dict2}
print(f"Cara 2 - Menggunakan unpacking: {dict3_unpack}")
print(" ")
print("----------------------------")

# ============================================================================
# BAGIAN 8: KOMBINASI (ADVANCED)
# ============================================================================

# Soal 20: Data Siswa
# Diberikan data siswa (gunakan list of dictionary):
# [
#   {'nama': 'Budi', 'nilai': 85},
#   {'nama': 'Ani', 'nilai': 92},
#   {'nama': 'Citra', 'nilai': 78}
# ]
# a) Cetak semua nama siswa
# b) Hitung rata-rata nilai semua siswa
# c) Cari siswa dengan nilai tertinggi
# d) Cetak siswa yang mendapat nilai di atas 80
# TODO: Tulis kode Anda di bawah
data_siswa = [
   {'nama': 'Ani', 'nilai': 92},
   {'nama': 'Citra', 'nilai': 78},
   {'nama': 'Budi', 'nilai': 85}
] 
for data in data_siswa:
    print(data['nama'])
def hitung_rata_rata_siswa(siswa_list):
    total_nilai = 0
    for siswa in siswa_list:
        total_nilai += siswa['nilai']
    rata_rata = total_nilai / len(siswa_list)
    return rata_rata
print(f"Rata-rata nilai semua siswa: {hitung_rata_rata_siswa(data_siswa)}")
siswa_tertinggi = max(data_siswa, key=lambda x: x['nilai'])
print(f"Siswa dengan nilai tertinggi: {siswa_tertinggi['nama']} dengan nilai {siswa_tertinggi['nilai']}")

print("Siswa yang mendapat nilai di atas 80:")
for siswa in data_siswa:
    if siswa['nilai'] > 80:
        print(f"{siswa['nama']} dengan nilai {siswa['nilai']}")
print(" ")
print("----------------------------")
# Soal 21: Cleaning Data (Seperti latihan Anda di latihan selasa.py)
# Diberikan data kotor:
# data = [
#   "NAma s4y4 4l1 R4hm4n",
#   "hAri iNi mErah",
#   "Saya suka PYTHON"
# ]
# Bersihkan data dengan:
# a) Ubah semua ke lowercase
# b) Ganti angka dengan huruf yang benar (4->a, 1->i, dst)
# c) Kapitalkan huruf pertama setiap kalimat
# TODO: Tulis kode Anda di bawah
data = [
   "NAma s4y4 4l1 R4hm4n",
   "hAri iNi mErah",
   "Saya suka PYTHON"
 ]
bersih = []
for kalimat in data:
    kalimat = kalimat.lower()
    kalimat = kalimat.replace("4", "a").replace("1", "i").replace("0", "o").replace("3", "e").replace("5", "s")
    kalimat = kalimat.capitalize()
    bersih.append(kalimat)
print("Data setelah dibersihkan:")
for b in bersih:
    print(b)
print(" ")
print("----------------------------")
# ============================================================================


# Soal 22: Challenge - Hitung Frekuensi Kata
# Diberikan string: "python python java python java c c c python"
# Hitung berapa kali setiap kata muncul dan tampilkan dalam format:
# python: 4 kali
# java: 2 kali
# c: 3 kali
# (Gunakan dictionary atau method count())
# TODO: Tulis kode Anda di bawah
kata = "python python java python java c c c python"
kata_list = kata.split(" ")
frekuensi = {}
for k in kata_list:
    if k in frekuensi:
        frekuensi[k] += 1
    else:
        frekuensi[k] = 1
for k, v in frekuensi.items():
    print(f"{k}: {v} kali")
print(" ")
print("------------------------------------------------------------------")
# ============================================================================

"""
================================================================================
TIPS MENGERJAKAN:
================================================================================
1. Baca soal dengan cermat
2. Mulai dari soal paling mudah (Bagian 1)
3. Test kode Anda dengan print() untuk melihat hasilnya
4. Jika stuck, coba break down menjadi langkah yang lebih kecil
5. Gunakan Google/ChatGPT untuk cari tahu konsep yang belum dipahami
6. Lakukan soal secara bertahap, jangan semua sekaligus

KONSEP YANG PERLU DIKUASAI:
- Variable, tipe data, operasi
- String methods (upper(), lower(), replace(), split(), join(), dll)
- List indexing, slicing, methods
- if-else, for loop, while loop
- Function definition dan calls
- Dictionary basics
- Kombinasi beberapa konsep di atas

GOOD LUCK! 💪
================================================================================
"""
