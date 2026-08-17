#replace
print("Hello, World!")
print("Hello, World!".replace("World", "Python"))
#jadi replace itu mengganti kata atau karakter tertentu dengan kata atau karakter lain dalam sebuah string


print("------------------------")  
print("str.isupper")
"""Mengembalikan True jika semua karakter alfabet dalam string 
adalah huruf kapital dan ada setidaknya satu karakter alfabet."""

print("HELLO".isupper())      # True
print("Hello".isupper())      # False
print("HELLO123".isupper())   # True (angka diabaikan)
print("123".isupper())        # False (tidak ada huruf sama sekali)
print("".isupper())           # False (string kosong)

print("------------------------")
print("str.islower")
"""Mengembalikan True jika semua karakter alfabet dalam string 
adalah huruf kecil dan ada setidaknya satu karakter alfabet."""

print("hello".islower())      # True
print("Hello".islower())      # False
print("hello123".islower())   # True
print("123".islower())        # False

print("------------------------")
print("str.isalpha")
"""Mengembalikan True jika semua karakter adalah 
huruf alfabet (a-z, A-Z) dan string tidak kosong."""

print("Hello".isalpha())      # True
print("Hello123".isalpha())   # False
print("Hello!".isalpha())     # False
print("".isalpha())           # False

print("------------------------")
print("str.isalnum")
"""Mengembalikan True jika semua karakter adalah
huruf atau angka (alfanumerik) dan string tidak kosong."""

print("Hello123".isalnum())    # True
print("Hello 123".isalnum())   # False (ada spasi)  
print("Hello!".isalnum())      # False (ada tanda seru)
print("".isalnum())            # False (string kosong)

print("-----------------------")
print("str.isdecimal")
"""Mengembalikan True hanya jika semua karakter adalah 
digit desimal (0-9) dan string tidak kosong."""

print("123".isdecimal())      # True
print("12.3".isdecimal())     # False (titik bukan digit)
print("½".isdecimal())        # False (meski angka, tapi bukan digit desimal biasa)
print("-12".isdecimal())      # False

print("----------------------")
print("str.isspace")
"""Mengembalikan True jika semua karakter adalah 
whitespace (spasi, tab \t, newline \n, dll) dan string tidak kosong."""

print("   ".isspace())        # True
print("\t\n".isspace())       # True
print(" a ".isspace())        # False (ada huruf 'a')
print("aku kamu".isspace())   # False

print("----------------------")
print("str.istitle")
"""Mengembalikan True jika setiap kata dimulai dengan huruf kapital 
dan sisanya huruf kecil (sesuai aturan judul), dan ada setidaknya satu karakter alfabet."""

print("Hello World".istitle())    # True
print("Hello world".istitle())    # False ('world' harus 'World')
print("Hello_World".istitle())    # True (underscore dianggap pemisah kata)
print("123 Hello".istitle())      # True ('123' diabaikan, 'Hello' benar)
print("Hello123".istitle())       # True ('123' di akhir tidak masalah)
print("HELLO".istitle())          # False (semua kapital → bukan title case)



text = "Apakah kamu suka python?!"
print(text.replace("python", "programming"))
print(" ")


# Mengganti satu kata
kalimat = "Saya suka kucing"
hasil = kalimat.replace("suka", "ga suka")
print(hasil)  # "Saya suka anjing"
print(kalimat)  # "Saya suka kucing" (string asli tidak berubah!)

#study kasus replace
#"..." (titik-titik berlebihan)
#"!!!" (tanda seru berlebih)
#Singkatan tidak konsisten: "gak", "nggak", "tdk"
print(" ")
ulasan = ["Saya suka banget python!!!",
          "Python itu keren banget....",
          "Saya nggak suka bug di kode tdk",
          "Belajar python itu menyenangkan!!!"
        ]

hasilBersih = []
for teks in ulasan:
    teks = teks.replace("!!!", "!")
    teks = teks.replace("nggak", "tidak")
    teks = teks.replace("tdk", "tidak")
    hasilBersih.append(teks)

for bersih in hasilBersih:
    print(bersih)
    
print(" ")

hewan = ["kucing tidak memiliki ekor",
         "kuda memiliki bulu lebat",
         "mnyt memiliki taring tajam",
         "kambing berlalri di atas pohon"]

copy = []
for b in hewan:
    b = b.replace("tidak memiliki", "memiliki")
    b = b.replace("bulu lebat", "kecepatan")
    b = b.replace("mnyt", "monyet")
    b = b.replace("taring tajam", "ekor pajang")
    b = b.replace("atas pohon", "padang rumput")
    copy.append(b)
    
for b in copy:
    print(b)
    
print("----------------------------")
print("studi kasus")
""" membuat fitur "Auto-Clean Text" untuk aplikasi editor teks.
Aturannya:

Pisahkan kalimat menjadi kata-kata (dipisah oleh spasi).
Untuk setiap kata:
Jika hanya terdiri dari huruf alfabet (isalpha() = True):
Jika semua huruf kapital → ubah ke huruf kecil semua.
Jika semua huruf kecil → biarkan.
Jika campuran (misal: UjangPrime) → tandai sebagai "Nama Diri", jangan ubah.
Jika mengandung angka/simbol → hapus kata tersebut.
Tujuan: hasil akhir adalah daftar kata yang bersih dan konsisten, kecuali nama diri yang sengaja dipertahankan.

"""

teks = "HELLO world UjangPrime test123 @code Python3 AI"

def bersihkan_kalimat(teks: str) -> list:
    kata_lits = teks.split(" ")
    hasil_bersih = []
    
    for kata in kata_lits:
        if not kata.isalpha():
            continue # Hapus kata dengan angka/simbol
        
        if kata.isupper():
            hasil_bersih.append(kata.lower())
        elif kata.islower():
            hasil_bersih.append(kata)
        else:
            hasil_bersih.append(kata) 
            
    return hasil_bersih

print(bersihkan_kalimat(teks))
print(" ")
print("----------------------------")

# Validasi Nama Pengguna
username1 = "user123"
username2 = "user_123"
username3 = "123"
username4 = ""

print(f"'{username1}'.isalnum(): {username1.isalnum()}")  # Output: True
print(f"'{username2}'.isalnum(): {username2.isalnum()}")  # Output: False (karena ada '_')
print(f"'{username3}'.isalnum(): {username3.isalnum()}")  # Output: True
print(f"'{username4}'.isalnum(): {username4.isalnum()}")  # Output: False (string kosong)

print("----------------------------")
# Validasi Kode Produk (hanya angka)
product_code1 = "12345"
product_code2 = "123.45"
product_code3 = "abc"
product_code4 = "😊😊😊" 

print(f"'{product_code1}'.isdecimal(): {product_code1.isdecimal()}")  # Output: True
print(f"'{product_code2}'.isdecimal(): {product_code2.isdecimal()}")  # Output: False (karena ada '.')
print(f"'{product_code3}'.isdecimal(): {product_code3.isdecimal()}")  # Output: False
print(f"'{product_code4}'.isdecimal(): {product_code4.isdecimal()}")  # Output: False
print(" ")
print("----------------------------")
# Validasi Input Kosong atau Hanya Spasi
user_input1 = "   "
user_input2 = "\t\n"
user_input3 = "hello world"
user_input4 = ""

print(f"'{user_input1}'.isspace(): {user_input1.isspace()}")  # Output: True
print(f"'{user_input2}'.isspace(): {user_input2.isspace()}")  # Output: True
print(f"'{user_input3}'.isspace(): {user_input3.isspace()}")  # Output: False
print(f"'{user_input4}'.isspace(): {user_input4.isspace()}")  # Output: False
print(" ")
print("----------------------------")
# Validasi Judul Artikel
article_title1 = "Belajar Python Dengan Mudah"
article_title2 = "belajar python dengan mudah"
article_title3 = "BELAJAR PYTHON DENGAN MUDAH"
article_title4 = "Belajar Python Dengan mudah" # 'mudah' tidak kapital
article_title5 = "Hello World"

print(f"'{article_title1}'.istitle(): {article_title1.istitle()}")  # Output: True
print(f"'{article_title2}'.istitle(): {article_title2.istitle()}")  # Output: False
print(f"'{article_title3}'.istitle(): {article_title3.istitle()}")  # Output: False
print(f"'{article_title4}'.istitle(): {article_title4.istitle()}")  # Output: False
print(f"'{article_title5}'.istitle(): {article_title5.istitle()}")  # Output: True
