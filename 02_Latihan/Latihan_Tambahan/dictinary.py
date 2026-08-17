data_hewan_qurban = {
    "spi": "sapi po",
    "sm":"sapi simental",
    "sl": "sapi limosin",
    "kc": "kambing kacang",
    "kb": "kambing boer"
    
}

# panjang dict
LANDICT = len(data_hewan_qurban)
print(f"banyak data pada data hewan qurbam = {LANDICT}")

# mengetahui key dalam dict

KEY = 'spi'
KEYCHECK = KEY in data_hewan_qurban
print(f'ini dalah key SPI = {KEYCHECK}')
 
print("data hewan qurban =  ", data_hewan_qurban.get("kc"))

data_copy = data_hewan_qurban.copy()
print(f"data hewan telah di copy {data_copy}")

data_hewan_qurban["kc"] = "kacang" # ga dicopy 
print(f"data ga di copy {data_hewan_qurban}")

data_sapi_simental = data_copy.pop("sm")
print(f"data pop = {data_sapi_simental}")
print(f"data setelah pop = {data_copy}") # sapi limosin di data ga ada menjadi keluar dari data dict

toko_bakti_qurban = {
    "sapi 1": {"nama": "sapi po","harga" : 27000000, "stok": 10}, 
    "sapi 2" : {"nama": "sapi simental", "harga": 47000000, "stok": 30},
    "kambing 1": {"nama": "kambing kacang", "harga": 8000000, "stok": 0},
    "kambing 2" : {"nama": "kambing boer", "harga": 8000000, "stok": 50},
}

print(f"==== datar data hewan qurban ====\n")

for data_qurban, isi in toko_bakti_qurban.items():  
    # tampilan menu
    print(f"kode {data_qurban}, jenis {isi['nama']},  harga {isi['harga']} ")
    
user_input = input("masukan katakunci hewan qurban (sapi 1,sapi 2,kambing 1, kambing 2 = ) ")
data_beli = toko_bakti_qurban.get(user_input)
if data_beli is None:
    print(f"data tidak ada di menu")
else:
    stok_saat_ini = data_beli["stok"]

    
    if  stok_saat_ini > 0:
      print(f"data qurban jenis {data_beli['nama']} dengan harga {data_beli['harga']} stok ready {data_beli['stok']}" )
    else:
     print(f"data qurban jenis {data_beli['nama']} dengan harga {data_beli['harga']} stok abis {data_beli['stok']}" )
    


