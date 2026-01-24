
#contoh soal 
# Validasi format email sederhana


# Untuk SETIAP email:
# 1. Cek apakah mengandung karakter "@"
# 2. Cek apakah diakhiri dengan ".com" ATAU ".co.id"
# Jika kedua syarat terpenuhi, print "Email valid"
# Jika tidak, print "Email tidak valid"

# Petunjuk: gunakan operator 'in' untuk cek "@"
# Petunjuk: gunakan operator 'or' untuk cek dua kemungkinan akhiran
email1 = "user@gmail.com"
email2 = "admin@yahoo.co.id"
email3 = "sales@outlook.com"

def validate_email(email):
    if "@" in email and (email.endswith(".com") or email.endswith(".co.id")):
        print("Email valid")
    else:
        print("Email tidak valid")  
validate_email(email1)  # Output: Email valid
validate_email(email2)  # Output: Email valid
validate_email(email3)  # Output: Email valid

# Bersihkan dan validasi kode booking

# Lakukan:
# 1. Hapus spasi di kiri dan kanan
# 2. Cek apakah dimulai dengan "BK-"
# 3. Cek apakah diakhiri dengan "-CONFIRMED"
# 4. Jika semua benar, print "Kode booking valid"
#    Jika tidak, print "Kode booking tidak valid"
booking = "   BK-2024-1234-CONFIRMED   "
if booking.strip(" ").startswith("BK-") and booking.endswith("-CONFIRMED"):
    print("Kode booking valid")
else:
    print("Kode booking tidak valid")

# Validasi username Instagram

# Untuk SETIAP username:
# 1. Jika dimulai dengan "@", hapus karakter @ dari kiri
# 2. Cek apakah setelah dibersihkan, username diakhiri dengan angka
# 3. Print hasilnya: True atau False

# Petunjuk: gunakan lstrip("@") untuk hapus @
# Petunjuk: gunakan [-1] untuk ambil karakter terakhir
# Petunjuk: gunakan .isdigit() untuk cek apakah angka
username1 = "@john_doe123"
username2 = "jane.smith"
username3 = "@_admin_"
def validate_username(username):
    cleaned_username = username.lstrip("@")
    print(cleaned_username[-1].isdigit())
validate_username(username1)  # Output: True
validate_username(username2)  # Output: False
validate_username(username3)  # Output: False   

#Join adalah metode untuk menggabungkan elemen-elemen dalam sebuah list/array menjadi satu string dengan pemisah tertentu.
#Split adalah metode untuk memecah sebuah string menjadi list/array berdasarkan pemisah tertentu.

hobi = ["membaca", "menulis", "berkebun"]
hasil = ", ".join(hobi)
print(hasil)  
print(" ")

data = "apel, maangga, pisang, jeruk "
hasil = data.split(", ")
print(hasil)

print(" ")
#soal latihan join dan split
print("soal latihan join dan split")
motto = "Berusaha-Berdoa-Bertawakal"
kata_kata = motto.split("-")
print(kata_kata)


#pisahkan username dan domain menggunakan split
#Pisahkan domain name dan ekstensi
#Gabungkan kembali dengan format: "username - domain - ekstensi"

email = "user@example.com"
# Langkah 1
bagian = email.split("@")  # ["user", "example.com"]
username = bagian[0]
domain_lengkap = bagian[1]


# Langkah 2
domain_bagian = domain_lengkap.split(".")  # ["example", "com"]
domain_name = domain_bagian[0]
ekstensi = domain_bagian[1]


# Langkah 3
hasil = " - ".join([username, domain_name, ekstensi])
print(hasil)  # "user - example - com"

#Buat program untuk mengubah format tanggal dari "02-11-2025" menjadi "02/11/2025"
tanggalLama = "02-11-2025"

bagian = tanggalLama.split("-")
tanggalBaru = "/".join(bagian)
print(tanggalBaru)  # Output: "02/11/2025"

#Join hanya bisa menggabungkan list yang berisi STRING
#Split tanpa parameter akan memisahkan berdasarkan whitespace apapun
"a  b\tc\nd".split()  # ["a", "b", "c", "d"]


