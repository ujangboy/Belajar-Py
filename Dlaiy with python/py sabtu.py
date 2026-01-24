#rstrip
# difinisi: Menghapus karakter tertentu dari akhir string
text = "Aku sayang kamu 100%"
print (text.rstrip("100%"))  # Output: "Aku

#lstrip
# difinisi : Menghapus karakter tertentu tetapi dari kiri
text = "aku tidak sayang kamu"
print(text.lstrip("aku"))  

#strip
# difinisi : menghapus spasi dan newline dari kedua sisi kanan dan kiri
text = "   Halo Dicoding!   \n"
print(text.strip())  # Output: "Halo Dicoding!" sayang kamu "
text = " aku sayang kamu "
print(text.strip(" aku "))  # Output: "sayang kamu"

#soal rstrip
text = "belajar python itu menyenangkan???"
print(text.rstrip("???"))

#soal lstrip
text = "###python adalah bahasa pemoragman###"
print(text.lstrip("###"))

#soal strip
text = "???selamat datang di python!!!!!"
print(text.strip("?!"))

print(" ")
print("...............")
#startswith 
#difinisi : memeriksa apakah string diawali dengan substring tertentu
''''
substring: Substring yang ingin diperiksa.
start (opsional): Indeks awal untuk memulai pencarian.
end (opsional): Indeks akhir untuk menghentikan pencarian.
'''
text = "Belajar Python itu menyenangkan"
print(text.startswith("belajar"))  # Output: True
print(text.startswith("kamu"))
print(text.startswith("Python", 8))  # Output: True (mulai dari indeks ke-8)

print( " ")
print("...............")
#endswith
#difinisi : memeriksa apakah string diakhiri dengan substring tertentu
'''
substring: Substring yang ingin diperiksa.
start (opsional): Indeks awal untuk memulai pencarian.
end (opsional): Indeks akhir untuk menghentikan pencarian.
'''
text ="Belajar python itu menyenangkan"
print(text.endswith("menyenangkan"))  # Output: True
print(text.endswith("kamu"))
print(text.endswith("python",0, 14))  
print(text[0:14])

print("...............")
#soal startswith
text = "Halo, selamat databg di dunia python"
print(text.startswith("Halo"))
print(text.startswith("selamat", 6))

#soal endswith
print(" ")
print("...............")
text = "belajar python itu menyengangkan sekali."
print(text.endswith("sekali."))
print(text.endswith("sekali", 0, 30))


print(" ")
print("soal latihan")
#latihan soal
# Cek apakah email diakhiri dengan "@gmail.com"
# Output yang diharapkan: True
email = "user@gmail.com"
print(email.endswith("@gmail.com"))

print(" ")
kode = "ID-12345-END"
# Cek apakah kode dimulai dengan "ID-" DAN diakhiri dengan "-END"
# Output yang diharapkan: True
print(kode.startswith("ID-")and kode.endswith("-END"))

teks = "   Hello World!!!   "
# Hapus spasi dari kiri saja, tapi biarkan yang kanan
# Output yang diharapkan: "Hello World!!!   "
print(teks.lstrip(" "))

''''
Buatlah fungsi validasi_username(username) yang:

Menghapus spasi di awal dan akhir
Mengecek apakah username dimulai dengan huruf (bukan angka)
Mengecek apakah username diakhiri dengan angka
Return True jika valid, False jika tidak
'''

validasi_usernamea = "username"
def validasi_username(username):
    username = username.strip()
    return username[0].isalpha() and username[-1].isdigit()
print(validasi_username("  user123  "))  
print(validasi_username("  123user  "))  
print(validasi_username("  user  "))






