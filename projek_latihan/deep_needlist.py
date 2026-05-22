list1 = [4, 5]
list2 = [6, 7]

nedted_lits2d = [list1, list2, 11] ## list dalam list
print("ini adalah nedted lits atau list 2d = ", nedted_lits2d) 

## mangambil data nedted list
mengambil_data = nedted_lits2d[1][0] ## [1] [6, 7] mangambil list dulu lalu baru mngambil data dalam list tersebut [0] sama dengan[6] mangambil dari [6, 7] 
print("mngambil data nedted list = ", mengambil_data)



data_copy = nedted_lits2d.copy()
print(f"data nedted lits copy = {data_copy}")

addres_list_asli = (hex(id(nedted_lits2d)))
addres_list_copy =  (hex(id(data_copy)))

print(f"addrees dari data list asli = {addres_list_asli}") # addes sama 0x242012f7b40
print(f"addrees dari data list copy = {addres_list_copy}\n") # addes sama 0x242012f7b40


addres_list_asli = (hex(id(nedted_lits2d[0][1])))
addres_list_copy =  (hex(id(data_copy[0][1])))
print("addres dari member ke-1")
print(f"addrees member list asli = {addres_list_asli}") 
print(f"addrees member list copy = {addres_list_copy}")

nedted_lits2d [1][0] = 1
nedted_lits2d[2] = 8
print(f"dari perubahan dalam list = {nedted_lits2d}")
print(f"dari perubahan luar list = {data_copy}")


# harus pake import 
from copy import deepcopy

data_deep = deepcopy(nedted_lits2d)
print(f"ini adalah data deep (sebelum diubah) = {data_deep}")

# SEKARANG ubah list asli SETELAH deepcopy
nedted_lits2d[1][0] = 999  # Ubah isi list anak
nedted_lits2d[2] = 777     # Ubah elemen luar

print(f"\nSetelah ubah list asli:")
print(f"nedted_lits2d = {nedted_lits2d}")  # Berubah jadi [[4, 5], [999, 7], 777]
print(f"data_deep     = {data_deep}")      # TETAP [[4, 5], [1, 7], 8] ← TIDAK BERUBAH!

# Cek address list anak
print(f"\nAddress list anak [1]:")
print(f"nedted_lits2d[1] = {hex(id(nedted_lits2d[1]))}")
print(f"data_deep[1]     = {hex(id(data_deep[1]))}")  # ← BEDA address!