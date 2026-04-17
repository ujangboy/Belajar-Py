# TextForge - Alat Analisis Teks Multifungsi
# Project menggabungkan semua materi string, operasi data koleksi, dan struktur kontrol

# ======================
# 1. INPUT & PEMBERSIHAN TEKS (Sabtu + Minggu)
# ======================
text = "  Halo, dunia! 123.  "

# Sabtu: Bersihkan spasi/punctuation
cleaned_text = text.strip().rstrip('.,!?;:')  # Hapus spasi & tanda baca di akhir
print("===== PEMBERSIHAN TEKS =====")
print("Teks Asli:", repr(text))
print("Teks Bersih:", repr(cleaned_text))
if cleaned_text.startswith("Halo"):
    print("✓ Validasi: Teks dimulai dengan 'Halo'")

# Minggu: Pisahkan & gabungkan teks
words = cleaned_text.split()  # Pisahkan menjadi daftar kata
print("\nKata Setelah Split:", words)
recombined_text = ' '.join(words)  # Gabungkan kembali menjadi kalimat
print("Teks Setelah Join:", repr(recombined_text))

# ======================
# 2. PEMROSESAN KATA (Senin + Selasa)
# ======================
print("\n===== PEMROSESAN KATA =====")
processed_words = []
for word in words:
    # Senin: Ganti karakter & cek properti
    if word.isalpha():  # Hanya huruf
        if word.isupper():
            word = word.lower()  # Ubah ke lowercase
        elif word.islower():
            word = word.replace('a', '@')  # Ganti 'a' dengan '@'
    processed_words.append(word)
print("Kata Diproses:", processed_words)

# Selasa: Format angka & raw string
formatted_words = [
    word.zfill(5) if word.isdecimal() else word  # Format angka dengan zfill()
    for word in processed_words
]
raw_path = r"C:\new_folder"  # Contoh raw string
print("\nKata Terformat (zfill):", formatted_words)
print("Raw String Path:", raw_path)

# ======================
# 3. ANALISIS DATA (Rabu + Kamis)
# ======================
print("\n===== ANALISIS DATA =====")
# Rabu: Hitung panjang & frekuensi
word_lengths = [len(word) for word in formatted_words]
max_len = max(word_lengths)
count_123 = formatted_words.count('00123')
print("Panjang kata terpanjang:", max_len)
print("Frekuensi '00123':", count_123)

# Kamis: Pertukaran variabel & pengurutan
if len(formatted_words) > 1:
    # Pertukaran elemen pertama & terakhir
    formatted_words[0], formatted_words[-1] = formatted_words[-1], formatted_words[0]
sorted_words = sorted(formatted_words, key=len)  # Urutkan berdasarkan panjang
print("\nSetelah pertukaran:", formatted_words)
print("Setelah pengurutan:", sorted_words)

# ======================
# 4. PENYIMPANAN HASIL (Jumat)
# ======================
print("\n===== PENYIMPANAN HASIL =====")
# Jumat: Simpan dalam 4 tipe data koleksi
word_list = formatted_words  # List (mutable)
word_tuple = tuple(word_list)  # Tuple (immutable)
word_set = set(word_list)  # Set (tanpa duplikat)
word_dict = {i: word for i, word in enumerate(word_list)}  # Dictionary

# Tampilkan hasil
print("\nTipe Data Koleksi:")
print("List:", word_list)
print("Tuple:", word_tuple)
print("Set:", word_set)
print("Dictionary:", word_dict)

# Perbandingan tipe data
print("\nPerbandingan Tipe Data:")
print("- List vs Tuple: List bisa diubah, Tuple tidak")
print("- Set menghilangkan duplikat:", set(['a', 'a']) == {'a'})
print("- Dictionary menyimpan indeks:", word_dict)