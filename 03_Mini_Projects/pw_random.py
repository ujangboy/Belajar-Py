import random

def generate_passwort(nama_depan, nama_belakang, tahun_lahir):
    
    bagian_depan = nama_depan[:3].lower()
    bagian_belakang = nama_belakang[-3:].lower()
    bagian_tahun = tahun_lahir[-2:]
    
    simbol = (['!', '@', '#', '$', '/', '&'])
    angka_acak = random.randint(10, 99)
     
    rekkomendasi = []
    
    res1 = random.choice(simbol) + bagian_depan + bagian_belakang + bagian_tahun + str(angka_acak)
    rekkomendasi.append(res1)
    
    res2 = bagian_depan.capitalize() + str(angka_acak) + bagian_belakang[::-1].lower() + bagian_tahun
    rekkomendasi.append(res2)
    
    shuffle_list = list(bagian_depan + bagian_belakang)
    random.shuffle(shuffle_list)
    shuffle_str = ''.join(shuffle_list)
    res3 = shuffle_str + random.choice(simbol) + str(angka_acak)
    rekkomendasi.append(res3)
    
    return rekkomendasi
    
def main():
    print("=== buat password otomatis ===")
    print("silahkan masukan data anda")
    
    nama_depan = input("nama depan: ").strip()
    nama_belakang = input("nama belakang: ").strip()
    tahun_lahir = input("tahun lahir: ").strip()
    
    if not (nama_depan and nama_belakang and tahun_lahir.isdigit()):
        print("\ninput tidak valid, pastikan semua data terisi dengan benar.")
        return
    
    print("\nRekomendasi password:")
    passwords = generate_passwort(nama_depan, nama_belakang, tahun_lahir)
    
    print("\n 3 rekomdasi password untuk anda:")
    for idx, pw in enumerate(passwords, 1,):
        print(f"{idx}. {pw}")
        
if __name__ == "__main__":
    main()    
   