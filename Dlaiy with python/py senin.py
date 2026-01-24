#Join adalah metode untuk menggabungkan elemen-elemen dalam sebuah list/array menjadi satu string dengan pemisah tertentu.
#Split adalah metode untuk memecah sebuah string menjadi list/array berdasarkan pemisah tertentu.

hobi = ["membaca", "menulis", "berkebun"]
hasil = "| ".join(hobi)
print(hasil)  
print(" ")

data = "apelmaanggapisangjeruk "
hasil = data.split("_")
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

tanggalold = "04-12-2025"
bagian2 = tanggalold.split("-")
tanggalNew = "/".join(bagian2)
print(tanggalNew)


dataBuah = "apel, mangga, pisang, jeruk"
buah = dataBuah.split(", ")
buahGabungan = "; ".join(buah)
gabungan2 = " - ".join(buah)
print(buah)
print(buahGabungan)
print(gabungan2)

daftar_buah = ['pisang', 'salak', 'durian']
hasil_join = ", ".join(daftar_buah)
print(hasil_join)