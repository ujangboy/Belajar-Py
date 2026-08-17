import datetime as dt

print("silahkan masukan tanggal halir, \ntabggal, bulan, tahun\,\n di bawah ini!")

tanggal = int(input(f"Masukan tanggal lahir \t:"))
bulan = int(input(f"Masukan bulan lahir \t:"))
tahun = int(input(f"Masukan tahun lahir \t:"))

tanggalLahir = dt.date(tahun, bulan, tanggal)
print(f"tanggal lahir anda: ", tanggalLahir)
print(f"harinya adalah: {tanggalLahir:%A}") # harinya

# menghitung tahun
"""kita harus tau hari ini dulu dengan membuat varibael hari_ini
lalu di kuang untuk mngetahui hari nya dalam tahun lahir nya lalu di kurang setelah
itu baru bisa di bagi"""
hari_ini = dt.date.today()
umur_hari = hari_ini - tanggalLahir
umur_tahun = umur_hari.days // 365
print(f"umur anda sekarang:  {umur_tahun} tahun")
