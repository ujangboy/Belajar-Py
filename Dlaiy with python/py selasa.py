#replace
print("Hello, World!")
print("Hello, World!".replace("World", "Python"))
#jadi replace itu mengganti kata atau karakter tertentu dengan kata atau karakter lain dalam sebuah string

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
    b =b.replace("taring tajam", "ekor pajang")
    b = b.replace("atas pohon", "padang rumput")
    copy.append(b)
    
for b in copy:
    print(b)
    