data = [3,4,5,5,7,1]

for angka in data :
    
    print("ANGKA ", angka)
    
# list comperhension
data = [2,3,4,5 , 'haii' , 2,4,5,6]
print(f'data comperhension {data}')

# Terlalu kompleks, susah dibaca
hasil = [x**2 if x > 5 else x**3 if x > 2 else x for x in range(10) if x % 2 == 0]

#  Lebih baik pakai for loop biasa
hasil = []
for x in range(10):
    if x % 2 == 0:
        if x > 5:
            hasil.append(x ** 2)
        elif x > 2:
            hasil.append(x ** 3)
        else:
            hasil.append(x)


# latihan
print('soal no 1')
nilai =  [85, 90, 78, 92, 88]
total = 0
for n in nilai:
    total += (n)
    
print(f'total dari nilai n = {total}\n')
   
print('soal no 2')
buah = ["apel", "mangga", "pisang", "anggur", "melon", "jeruk"]
for panjang in buah:
    if len(panjang) > 5:
     print(panjang)
     
print('soal no 3')
angka = [12, 7, 23, 5, 18, 9, 30, 15]

hasil = []
for a in angka:
    if a > 10:
        hasil.append(a)
print(f'\nlebih besar dari 10 = {hasil}')
