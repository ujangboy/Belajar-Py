""""ganti list buah ini dengan list sayuran
2. ubah elemen pertama dan ke 3 dari list"""

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
