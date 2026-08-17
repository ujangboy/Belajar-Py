# MULTIKEYS & NESTED DICTIONARY
# Sebuah dictionary bisa bersarang (isinya adalah dictionary lagi)
# Dan juga dictionary bisa digunakan untuk mengelompokkan data yang kompleks.

import datetime

print("==== MULTIKEYS (NESTED DICTIONARY) ====")

mahasiswa1 = {
    "nama": "Ujang",
    "nim": "1001",
    "sks": 144,
    "lahir": datetime.datetime(2001, 4, 10)
}

mahasiswa2 = {
    "nama": "Asep",
    "nim": "1002",
    "sks": 140,
    "lahir": datetime.datetime(2002, 10, 10)
}

mahasiswa3 = {
    "nama": "Dadang",
    "nim": "1003",
    "sks": 100,
    "lahir": datetime.datetime(2000, 2, 29)
}

# Dictionary yang menampung dictionary mahasiswa di atas
data_mahasiswa = {
    "MAH001": mahasiswa1,
    "MAH002": mahasiswa2,
    "MAH003": mahasiswa3
}

print(f"Data Keseluruhan: \n{data_mahasiswa}\n")

print("==== LOOPING NESTED DICTIONARY ====")
# Mari kita buat tampilannya menjadi rapi seperti tabel
print(f"{'KEY':<8} {'NAMA':<10} {'SKS':<4} {'LAHIR':<10}")
print("-" * 40)

for mahasiswa in data_mahasiswa: # 'mahasiswa' disini adalah key (MAH001, dsb)
    KEY = mahasiswa
    
    # Mengambil nested dictionary-nya
    NAMA = data_mahasiswa[KEY]['nama']
    SKS = data_mahasiswa[KEY]['sks']
    
    # Format waktu lahir
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x") # %x = tanggal lokal
    
    print(f"{KEY:<8} {NAMA:<10} {SKS:<4} {LAHIR:<10}")

# Catatan Tambahan:
# Jika kamu menggunakan nested dictionary yang sangat dalam (misal dict dalam dict dalam dict), 
# jika ingin di-copy secara penuh agar tidak saling terkait memorinya, 
# kamu harus menggunakan `deepcopy` dari module `copy`.
