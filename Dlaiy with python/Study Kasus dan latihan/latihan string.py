""""ganti list buah ini dengan list sayuran
    ubah elemen pertama dan ke 3 dari list"""

list_buah = ["manggga", "apel", "pisang", "semangka"]
list_sayur = []
for buah in list_buah:
    if buah == "manggga":
        buah = "bayam"
    elif buah == "pisang":
        buah = "kangkung"
    elif buah ==  "apel":
        buah = "wortel"
    elif buah == "semangka":
        buah = "selada" 
    list_sayur.append(buah)
print(list_sayur)

list_buah = ["manggga", "apel", "pisang", "semangka"]
list_buah[0] = "bayam"
list_buah[2] = "kangkung"
print(list_buah)


# rapihkan kalimat
kalimat = ["Mobil RUsak Karna BATu",
           "s4ya makan 4pel dan mangga",
           "nomer rumah 234b",
           "aku @*^% dengan dia"
           ]
kalimat_bersih = []
for kata in kalimat:
    kata = kata.replace("RUsak", "rusak")
    kata = kata.replace("BATu", "batu") 
    kata = kata.replace("Karna", "karena")  
    kata = kata.replace("s4ya", "saya")
    kata = kata.replace("4pel", "apel")
    kata = kata.replace("234b", "234")
    kata = kata.replace(" @*^%","")

    kalimat_bersih.append(kata)
print(kalimat_bersih)

cek_kalimat = [
    "Halo Dunia",
    "HALO DUNIA",
    "halo dunia",
    "Halo123",
    "12345",
    "   ",
    "Halo Dunia!",
    "ABC123XYZ"
]
    
cek_bersih =[]
for bersih in cek_kalimat:
    if bersih.isalpha():
       cek_bersih.append(bersih)
    elif bersih.isupper():
        cek_bersih.append(bersih.lower())
    elif bersih.islower():
        cek_bersih.append(bersih)
    elif bersih.isalnum():
        cek_bersih.append(bersih)
    elif bersih.isdecimal():
        cek_bersih.append(bersih)
    elif bersih.isspace():
        cek_bersih.append(bersih)
    elif not bersih.isalpha():
        continue # Hapus kata dengan angka/simbol   
    
print(cek_bersih)
print(" ")
print("----------------------------")    

"""
LATIHAN FUNDAMENTAL PYTHON - STRING METHODS
==========================================
Format TODO - Tulis kode Anda sendiri!
"""

# ================================
# TODO 1: REPLACE() - Mengganti teks
# ================================
# Soal: Ganti semua kata "python" dengan "javascript" dari string di bawah
# Tambahkan kode Anda di sini:

teks = "python adalah bahasa python yang menarik untuk python programming"
# TODO: Ganti "python" dengan "javascript"


print("\n" + "=" * 60)

# ================================
# TODO 2: ISUPPER() - Cek huruf besar
# ================================
# Soal: Buat program untuk cek apakah variabel HELLO adalah uppercase
# Tambahkan kode Anda di sini:

kata = "HELLO"
# TODO: Gunakan isupper() untuk cek dan print hasilnya


print("\n" + "=" * 60)

# ================================
# TODO 3: ISLOWER() - Cek huruf kecil
# ================================
# Soal: Cek apakah "helloworld" adalah lowercase
# Tambahkan kode Anda di sini:

text = "helloworld"
# TODO: Gunakan islower() dan tampilkan hasilnya


print("\n" + "=" * 60)

# ================================
# TODO 4: ISALPHA() - Cek hanya huruf
# ================================
# Soal: Dari list di bawah, tampilkan mana yang hanya berisi huruf
# Tambahkan kode Anda di sini:

data = ["python", "python123", "coding", "program!"]
# TODO: Loop melalui list, cek dengan isalpha(), print hasilnya


print("\n" + "=" * 60)

# ================================
# TODO 5: ISALNUM() - Cek huruf/angka
# ================================
# Soal: Validasi apakah password "pass123" valid (hanya huruf & angka)
# Tambahkan kode Anda di sini:

password = "pass123"
# TODO: Cek dengan isalnum() dan print "Valid" atau "Invalid"


print("\n" + "=" * 60)

# ================================
# TODO 6: ISDECIMAL() - Cek hanya angka
# ================================
# Soal: Dari list ["123", "12.5", "12a", "999"], mana yang pure decimal?
# Tambahkan kode Anda di sini:

numbers = ["123", "12.5", "12a", "999"]
# TODO: Loop dan cek dengan isdecimal(), print yang valid


print("\n" + "=" * 60)

# ================================
# TODO 7: ISSPACE() - Cek whitespace
# ================================
# Soal: Cek apakah string "   " (3 spasi) adalah whitespace
# Tambahkan kode Anda di sini:

spasi = "   "
# TODO: Gunakan isspace() dan print hasilnya


print("\n" + "=" * 60)

# ================================
# TODO 8: ISTITLE() - Cek Title Case
# ================================
# Soal: Dari list di bawah, mana yang sudah Title Case?
# Tambahkan kode Anda di sini:

judul_list = ["Hello World", "hello world", "Python Programming", "PYTHON"]
# TODO: Loop dan cek dengan istitle(), print hasilnya


print("\n" + "=" * 60)

# ================================
# TODO 9: KOMBINASI - Validasi Username
# ================================
# Soal: Buat validasi username dengan kriteria:
#       - Minimal 5 karakter
#       - Hanya huruf dan angka (isalnum)
#       - Tidak boleh semua huruf besar (not isupper)
# Tambahkan kode Anda di sini:

username_test = ["python", "PY", "python123", "PY@THON", "mycode2024"]
# TODO: Validasi setiap username sesuai kriteria di atas


print("\n" + "=" * 60)

# ================================
# TODO 10: KOMBINASI - Cek Kalimat Valid
# ================================
# Soal: Cek apakah kalimat "Hello World" adalah Title Case 
#       DAN tidak ada simbol khusus (hanya spasi & huruf)
# Tambahkan kode Anda di sini:

kalimat = "Hello World"
# TODO: Gunakan istitle() dan kombinasi method lain untuk validasi


print("\n" + "=" * 60)

# ================================
# TODO 11: KOMBINASI - Clean & Validate Data
# ================================
# Soal: Dari list data di bawah:
#       - Bersihkan whitespace di awal/akhir (gunakan strip())
#       - Cek apakah hanya berisi huruf
#       - Ubah ke uppercase jika valid
# Tambahkan kode Anda di sini:

data_raw = ["  python  ", "  coding123  ", "  programming  ", "  !special!  "]
# TODO: Clean, validasi dengan isalpha(), dan uppercase jika valid


print("\n" + "=" * 60)

# ================================
# TODO 12: KOMBINASI - Identifikasi Tipe Data
# ================================
# Soal: Dari list mixed_data di bawah, identifikasi tipe setiap elemen:
#       - Jika pure huruf → "HURUF"
#       - Jika pure angka → "ANGKA"
#       - Jika huruf + angka → "ALFANUMERIK"
#       - Jika hanya spasi → "WHITESPACE"
#       - Lainnya → "CAMPURAN"
# Tambahkan kode Anda di sini:

mixed_data = ["python", "12345", "python123", "   ", "hello@world"]
# TODO: Loop dan identifikasi tipe setiap data


print("\n" + "=" * 60)

# ================================
# TODO 13: KOMBINASI - Replace & Validasi
# ================================
# Soal: String "PYTHON programming" 
#       1. Ganti "python" dengan "java" (case-insensitive hint: gunakan lower())
#       2. Cek apakah hasil akhir adalah Title Case
# Tambahkan kode Anda di sini:

text_original = "PYTHON programming"
# TODO: Replace dan cek hasilnya dengan istitle()


print("\n" + "=" * 60)

# ================================
# TODO 14: KOMBINASI - Form Validator
# ================================
# Soal: Buat validasi form dengan rules:
#       - Email: hanya huruf, angka, @, dan . (gunakan isalnum)
#       - Password: minimal 8 karakter, ada huruf besar & angka
#       - Phone: hanya angka, minimal 10 digit
# Tambahkan kode Anda di sini:

email = "user@gmail.com"
password = "MyPass123"
phone = "08123456789"
# TODO: Validasi ketiga field di atas


print("\n" + "=" * 60)

# ================================
# TODO 15: KOMBINASI - Text Formatter
# ================================
# Soal: Buat formatter untuk list kata di bawah:
#       - Jika lowercase → ubah ke Title Case dengan replace jika ada underscore
#       - Jika uppercase → turun ke lowercase
#       - Tampilkan status perubahan
# Tambahkan kode Anda di sini:

words = ["hello_world", "PYTHON", "coding Language"]
# TODO: Format setiap kata sesuai aturan di atas


print("\n" + "=" * 60)
print("SELESAI! Cek semua TODO di atas ✓")
print("=" * 60)
