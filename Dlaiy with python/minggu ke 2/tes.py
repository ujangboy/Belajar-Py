def perkenalkan(nama="Asep suyatna"):
    print("hala, " + nama + "!")


perkenalkan()
perkenalkan("fuji")

def deskripsi(nama, usia):
    print(f"saya{nama}, berusia{usia} tahun.")

deskripsi(usia=20, nama="Asep")

def tampilkan_nama(*args):
    for nama in args:
        print(nama)

tampilkan_nama("fuji", "senda", "angga")

def tampilkan_info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}:")
print(" ")
print("================================")

def tampilkan_info (**kwrgs):
    for k, v in kwrgs.items():
        print(f"{k}: {v}")
        
tampilkan_info(nama="asep", usia=20,
               kota="tangsel") 

def info(nama, usia=0, *args, **kwargs):
    print(f"nama:  {nama}, usia: {usia}")
    print(f"argumen tambahan: ", args )
    print("keyword argumen:" , kwargs)
    
info("asep", 20, "hobi: mengambar", kota="tangel",
pekerjaan= "programmer")

print(" ")
print("================================")
def tambahkan_elemen(arr):
    arr.append(100)
    
data = [1,2,3]
tambahkan_elemen(data)
print(data)

print(" ")
print("================================")
