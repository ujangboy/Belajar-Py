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
    "Hello_World"
]
    
cek_bersih =[]
for bersih in cek_kalimat:
    if bersih.isalnum() or bersih.isspace():
        continue
    if any(not c.isalnum() and not c.isspace() for c in bersih):
        continue
    if not any(c.isupper() for c in bersih):
        continue
    cek_bersih.append(bersih)
    
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
bersihkan_teks = teks.replace("python", "javascript")
print(bersihkan_teks)

print("\n" + "=" * 60)

# ================================
# TODO 2: ISUPPER() - Cek huruf besar
# ================================
# Soal: Buat program untuk cek apakah variabel HELLO adalah uppercase
# Tambahkan kode Anda di sini:

kata = "HELLO"
# TODO: Gunakan isupper() untuk cek dan print hasilnya
cek_kata = kata.isupper()
print(cek_kata)

print("\n" + "=" * 60)

# ================================
# TODO 3: ISLOWER() - Cek huruf kecil
# ================================
# Soal: Cek apakah "helloworld" adalah lowercase
# Tambahkan kode Anda di sini:

text = "helloworld"
# TODO: Gunakan islower() dan tampilkan hasilnya
cek_lower = text.islower()
print(cek_lower)

print("\n" + "=" * 60)

# ================================
# TODO 4: ISALPHA() - Cek hanya huruf
# ================================
# Soal: Dari list di bawah, tampilkan mana yang hanya berisi huruf
# Tambahkan kode Anda di sini:

data = ["python", "python123", "coding", "program!"]
# TODO: Loop melalui list, cek dengan isalpha(), print hasilnya
hanyaHuruf = []
for item in data:
    if item.isalpha():
        hanyaHuruf.append(item)
print(hanyaHuruf)
        
print("\n" + "=" * 60)

# ================================
# TODO 5: ISALNUM() - Cek huruf/angka
# ================================
# Soal: Validasi apakah password "pass123" valid (hanya huruf & angka)
# Tambahkan kode Anda di sini:

password = "pass123"
# TODO: Cek dengan isalnum() dan print "Valid" atau "Invalid"
for char in password:
    if password.isalnum():
        print("Valid")
        break
    else:
        print("Invalid")
        break


print("\n" + "=" * 60)

# ================================
# TODO 6: ISDECIMAL() - Cek hanya angka
# ================================
# Soal: Dari list ["123", "12.5", "12a", "999"], mana yang pure decimal?
# Tambahkan kode Anda di sini:

numbers = ["123", "12.5", "12a", "999"]
# TODO: Loop dan cek dengan isdecimal(), print yang valid
hanya_decimal = []
for angka_desimal in numbers:
    if angka_desimal.isdecimal():
        hanya_decimal.append(angka_desimal)
print(hanya_decimal)
#ada yang versi ebih enak di baca 
hanya_decimal = [n for n in numbers if n.isdecimal()]
print(hanya_decimal)

print("\n" + "=" * 60)

# ================================
# TODO 7: ISSPACE() - Cek whitespace
# ================================
# Soal: Cek apakah string "   " (3 spasi) adalah whitespace
# Tambahkan kode Anda di sini:

spasi = "   "
# TODO: Gunakan isspace() dan print hasilnya
cek_spasi = spasi.isspace()
print(cek_spasi)

print("\n" + "=" * 60)

# ================================
# TODO 8: ISTITLE() - Cek Title Case
# ================================
# Soal: Dari list di bawah, mana yang sudah Title Case?
# Tambahkan kode Anda di sini:

judul_list = ["Hello World", "hello world", "Python Programming", "PYTHON"]
# TODO: Loop dan cek dengan istitle(), print hasilnya
cek_title = []
for judul in judul_list:
    if judul.istitle():
        cek_title.append(judul)
print(cek_title)
#ada yang lebih enak di baca
cek_title = [j for j in judul_list if j.istitle()]
print(cek_title)

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
validasi = []
for validasi_username in username_test:
    if (len(validasi_username) >= 5):
        if validasi_username.isalnum():
            if not validasi_username.isupper():
                validasi.append(validasi_username)
print(validasi)
# ada yang lebih enak di baca
validasi = [
    user for user in username_test
    if len(user) >= 5 and user.isalnum() and not user.isupper()
]

print("\n" + "=" * 60)

# ================================
# TODO 10: KOMBINASI - Cek Kalimat Valid
# ================================
# Soal: Cek apakah kalimat "Hello World" adalah Title Case 
#       DAN tidak ada simbol khusus (hanya spasi & huruf)
# Tambahkan kode Anda di sini:

kalimat = "Hello World"
# TODO: Gunakan istitle() dan kombinasi method lain untuk validasi
cek_title_case = kalimat.istitle()
cek_simbol = kalimat.isalpha()
cek_spasi = kalimat.isspace()
print(cek_title_case)   
print(cek_simbol)      # salah 
print(cek_spasi)       # salah
print("yang sudah di koreksi")
# koreksi labih jelas
cek_title_case = kalimat.istitle()
cek_hanya_huruf_dan_spasi = all(c.isalpha() or c.isspace() for c in kalimat)
valid = cek_title_case and cek_hanya_huruf_dan_spasi
print(valid)

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
filter_data = []
for filter in data_raw:
    bersih = filter.strip()
    if bersih.isalpha():
        filter_data.append(bersih.upper()) # typo harus uppercase
print(filter_data)
          
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
for camouran_data in mixed_data:
    bersih = camouran_data.strip()
    if bersih.isalpha():
        print(f"{bersih}: HURUF")
    elif bersih.isdecimal():
        print(f"{bersih}: ANGKA")
    elif bersih.isalnum():
        print(f"{bersih}: ALFANUMERIK")
    elif bersih.isspace():
        print(f"{bersih}: WHITESPACE")
    else:
        print(f"{bersih}: CAMPURAN")
    

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
cek_replace = text_original.lower().replace("python", "java")
cek_text_title =cek_replace.istitle()
 
print(cek_text_title)

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
valid_email = all(c.isalnum() or c in "@" or c == "." for c in email)
valid_password = (len(password) >= 8 and 
                  any(c.isupper() for c in password) and 
                  any(c.isdigit() for c in password))
valid_phone = (phone.isdecimal() and len(phone) >= 10)
print(f"Email valid: {valid_email}")
print(f"Password valid: {valid_password}")
print(f"Phone valid: {valid_phone}")

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
for valid in words:
    if valid.islower():
        format = valid.replace("_", " ").title()
        print(f"before {valid}", f"after {format}")
    elif valid.isupper():
        format = valid.lower()
        print(f"before {valid}", f"after {format}")
  
    else:
        valid.replace("_", " ").istitle()
        format = valid.replace("_", " ")
        print(f"before {valid}", f"after {format}")
    

print("\n" + "=" * 60)
print("SELESAI! Cek semua TODO di atas ✓")
print("=" * 60)
print(" ")

print("latihan 2 ")

# ================================
# TODO 1: GANTI KATA
# ================================
# Soal: Ganti semua kata "python" menjadi "java" dalam string berikut,
#       lalu ubah ke uppercase.
# Input: "Belajar python itu menyenangkan, python mudah dipelajari."
# Output: "BELAJAR JAVA ITU MENYENANGKAN, JAVA MUDAH DIPELAJARI."

# Tambahkan kode Anda di sini:

text1 = "Belajar python itu menyenangkan, python mudah dipelajari."
# Jawaban Anda:
ganti_kata = text1.replace("python", "java").upper()
print(ganti_kata)

print("=" * 50)

# ================================
# TODO 2: VALIDASI USERNAME
# ================================
# Soal: Dari list username berikut, tampilkan yang:
#       - Panjang minimal 5 karakter
#       - Hanya mengandung huruf dan angka
#       - Tidak semua huruf besar
# Tambahkan kode Anda di sini:

usernames = ["alice123", "BOB", "charlie", "dave42", "EVA2", "user_name", "py123"]
# Jawaban Anda:
valid_usernames = []
for name in usernames:
    #untuk panjang karekter miniml 5, name.isalnum hanya huruf dan angka, tidak semua huruf besar
    if (len(name) >=5 and name.isalnum() and not name.isupper()):
        valid_usernames.append(name)
print(valid_usernames)

print("=" * 50)

# ================================
# TODO 3: FILTER KATA
# ================================
# Soal: Dari list berikut, ambil hanya yang:
#       - Hanya berisi huruf
#       - Huruf pertama kapital
#       - Panjang lebih dari 3 karakter
# Tambahkan kode Anda di sini:

words = ["Apple", "banana", "Cherry", "Date", "elephant", "Fig", "Grape"]
# Jawaban Anda:
for word in words:
    if word.isalpha() and word.istitle() and len(word) > 3:
        print(word)

print("=" * 50)

# ================================
# TODO 4: FORMAT TEKS
# ================================
# Soal: Dari list berikut, ubah setiap item menjadi:
#       - Jika hanya huruf → ubah ke uppercase
#       - Jika mengandung angka → hapus angkanya dan ubah ke title case
#       - Jika hanya angka → ubah ke "NUMBER"
# Tambahkan kode Anda di sini:

mixed_list = ["hello", "world123", "456", "coding", "test789"]
# Jawaban Anda:
for ubah in mixed_list:
    if ubah.isalpha():
        bener = ubah.upper()
    elif ubah.isdecimal():
        bener = "NUMBER"
    else: 
        bukan_angka = ''.join([c for c in ubah if not c.isdigit()])
        bener = bukan_angka.title()
    print(bener)


print("=" * 50)

# ================================
# TODO 5: CEK SIMBOL
# ================================
# Soal: Dari list berikut, tampilkan yang TIDAK mengandung simbol apapun.
#       (hanya huruf, angka, dan spasi)
# Tambahkan kode Anda di sini:

items = ["Hello World", "Test123", "Special!", "Code Python", "Bug@Here"]
# Jawaban Anda:
for item in items:
    if all(c.isalnum() or c.isspace() for c in item):
        print(item)

print("=" * 50)
