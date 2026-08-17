def sequential_search(arr, key):
    for i in range(len(arr)):
        current_value = arr[i]
        if current_value == key:
         return i
    return -1
data_array = [29, 759, 77, 66, 99, 100]
print("---")
print("Program Sequential Search")
print("---")
print(f"Array data: {data_array}")

while True:
        try:
            search_key = int(input("\nMasukkan angka yang ingin dicari (atau ketik -1 untuk keluar): "))
            if search_key == -1:
                print("Terima kasih!")
                break
            hasil_pencarian = sequential_search(data_array, search_key)
            if hasil_pencarian != -1:
                print(f"Hasil Akhir: Angka {search_key} ditemukan pada indeks {hasil_pencarian}.")
            else:
                print(f"Hasil Akhir: Angka {search_key} tidak ditemukan dalam array.")
        except ValueError:
            print("Input tidak valid. Harap masukkan bilang bulat.")