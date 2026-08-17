import datetime 

warga_rt_07 = {
    "nama" : "amelia",
    "umur" : 20,
    "alamat" : "jl. rara no 8",
    "alamat lama" : False,
    "tanggal lahir" : datetime.datetime(2003,5,20)
}

warga_rt_08 = {
    "nama" : "joni",
    "umur" : "30",
    "alamat" : "jl. rara no 02",
    "alamat lama" : True,
    "tanggal lahir" : datetime.datetime(200, 4, 7)
}

warga_rt_06 = {
    "nama" : "ginanjar",
    "umur" : "33",
    "alamat" : "jl. rara no 44",
    "alamat lama" : False,
    "tanggal lahir" : datetime.datetime(2001, 12, 6)
}

data_warga_dusun_kiko = {
    'warga 06' : warga_rt_06,
    'warga 07' : warga_rt_07,
    'warga 08' : warga_rt_08
}

# data warga
print(f"{'key':<13} {"nama":<13} {"umur":<13}  {"alamat":<20} {"tanggal lahir":<25}")
print("-"*77)

for data_warga in data_warga_dusun_kiko:
    KEY = data_warga
    
    NAMA = data_warga_dusun_kiko[KEY]["nama"]
    UMUR = data_warga_dusun_kiko[KEY]["umur"]
    TANGGAL_LAHIR =data_warga_dusun_kiko[KEY]["tanggal lahir"].strftime("%x")
    ALAMAT = data_warga_dusun_kiko[KEY]["alamat"]

    print(f" {KEY:^6} {NAMA:^10} {UMUR:^17}  {ALAMAT:^17} {TANGGAL_LAHIR:^25}")