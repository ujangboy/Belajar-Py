"""latihan SORT dan SORTED di Python
materi ada di hari kamis pada file Py kamis.py

#srot adalah untuk mengurutkan elemen dalam lits atau array secara ascending atau descending
#sorted adalah fungsi yang mengembalikan list baru yang sudah diurutkan tanpa mengubah list asli
"""
# ================================
# TODO 1: SORT vs SORTED
# ================================
# Soal: Urutkan list berikut secara ascending:
#       - Gunakan .sort() untuk mengubah list asli
#       - Gunakan sorted() untuk membuat list baru
# Input:
numbers = [64, 34, 25, 12, 22, 11, 90]
# Jawaban Anda:
print("Urutan dengan sort():")
numbers.sort()
print(numbers) 

sorted_numbers = sorted(numbers)
print(sorted_numbers)

print("=" * 50)

# ================================
# TODO 2: URUTKAN KATA
# ================================
# Soal: Dari list kata berikut, urutkan berdasarkan panjang kata (pendek ke panjang)
#       Gunakan sorted() agar list asli tidak berubah
# Input:
words = ["python", "java", "go", "javascript", "c"]
# Jawaban Anda:
sprted_words = sorted(words, key=len) # key membuat python mengintruksikan dan len yang akan di intruksikan yaitu menghitung jumlah elemen pada lits
print(sprted_words)

print("=" * 50)

# ================================
# TODO 3: URUTKAN STRING SECARA TERBALIK
# ================================
# Soal: Urutkan string "python" secara descending (dari z ke a)
#       Gunakan sorted() dan join hasilnya
# Input:
text = "python"
# Jawaban Anda:
sorted_text = ''.join(sorted(text, reverse=True))  # reverse jika awalnya adalah false yaitu mengitungkan dari kecil ke besar adanya = true akan kebalikan cara hitungnya dari besar ke kecil
# sedengkan ''. adalah pimisah karna di sini tidak ada jadi kosongkan saja join untuk mengembalikan lits menjadi string menyatu.
print(sorted_text)

print("=" * 50)

# ================================
# TODO 4: FILTER DAN SORTIR
# ================================
# Soal: Dari list berikut, ambil hanya angka genap, lalu urutkan secara descending
#       Gunakan list comprehension dan sort/sorted
# Input:
numbers = [23, 45, 12, 67, 8, 90, 4, 33]
# Jawaban Anda:
even_numbers = [num for num in numbers if num % 2 == 0]
even_numbers.sort(reverse=True)
print(even_numbers)


print("=" * 50)

# ================================
# TODO 5: SORTIR BERDASARKAN NILAI ABSOLUT
# ================================
# Soal: Urutkan list berikut berdasarkan nilai absolut (tanpa tanda negatif)
#       Gunakan sorted() dengan key=abs
# Input:
numbers = [-20, 15, -5, 30, -10]
# Jawaban Anda:
sorted_by_abs = sorted(numbers, key=abs)
print(sorted_by_abs)
# jadi abs adalah mengurutkan berdasarkan absolut bagaimana caranya?
# jadi minusnya di ilangin pada porses abs dan abs menjadi angka terdekat dengan 0 yaitu 5 dan akan menjadi -5 lagi jika sudah ketemu 
# tidak mengubah hasil hanya saya menjadikan patokan cara mengurutan dari kecil ke besar

print("=" * 50)