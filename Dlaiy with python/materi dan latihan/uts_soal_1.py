def linear_search(data, target):
    
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


daftar_angka = [20, 30, 50, 70, 80]

print(f"dartar angka: {daftar_angka}")
target_angka = int(input("Masukkan angka yang ingin dicari: "))



hasil = linear_search(daftar_angka, target_angka)


if hasil != -1:       
    print(f"Angka {target_angka} ditemukan pada indeks ke-{hasil}.")
else:
    print(f"Angka {target_angka} tidak ditemukan dalam daftar.") 