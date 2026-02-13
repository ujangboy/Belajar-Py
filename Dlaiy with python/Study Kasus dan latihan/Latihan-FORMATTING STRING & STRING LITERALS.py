# ================================
# TODO 1: ZFILL
# ================================
# Soal: Tambahkan leading zero agar panjang string menjadi 5 karakter
# Input: "42"
# Output: "00042"
# Jawaban Anda:
number_str = "42"
panjang_5 = number_str.zfill(5)
print(panjang_5)

print("=" * 50)

# ================================
# TODO 2: RJUST
# ================================
# Soal: Rata kanan string "python" dalam kolom 10 karakter, isi dengan "*"
# Input: "python"
# Output: "****python"
# Jawaban Anda:
word = "python"
rata_kanan = word.rjust(10, '*')
print(rata_kanan)

print("=" * 50)

# ================================
# TODO 3: LJUST
# ================================
# Soal: Rata kiri string "code" dalam kolom 8 karakter, isi dengan "_"
# Input: "code"
# Output: "code____"
# Jawaban Anda:
word = "code"
rata_kiri = word.ljust(8, '_')
print(rata_kiri)

print("=" * 50)

# ================================
# TODO 4: CENTER
# ================================
# Soal: Tengahkan string "hello" dalam kolom 11 karakter, isi dengan "-"
# Input: "hello"
# Output: "---hello---"
# Jawaban Anda:
word = "hello"
hello_center = word.center(11, '-')
print(hello_center)

print("=" * 50)

# ================================
# TODO 5: ZFILL DENGAN NEGATIF
# ================================
# Soal: Gunakan zfill untuk "-42" agar panjangnya 6 karakter
# Input: "-42"
# Output: "-00042"
# Jawaban Anda:
neg_number = "-42"
negatif_zfill = neg_number.zfill(6)
print(negatif_zfill)
print("=" * 50)

# ================================
# TODO 6: STRING LITERAL - NEWLINE
# ================================
# Soal: Cetak dua baris: "Baris 1" dan "Baris 2" dalam satu string literal
# Jawaban Anda:
# ...

print("=" * 50)

# ================================
# TODO 7: STRING LITERAL - TAB
# ================================
# Soal: Cetak "Item 1" dan "Item 2" dengan tab di antaranya
# Jawaban Anda:
# ...

print("=" * 50)

# ================================
# TODO 8: RAW STRING
# ================================
# Soal: Cetak string berikut tanpa escape sequence: "Path: C:\new\folder"
# Gunakan raw string
# Jawaban Anda:
path = r""
# ...

print("=" * 50)

# ================================
# TODO 9: GABUNGAN FORMAT
# ================================
# Soal: Format string "id" menjadi 4 karakter dengan leading zero, lalu tengahkan dalam 10 karakter
# Input: "7"
# Output: "0004"
# Lalu: tengahkan dalam 10 karakter dengan "*"
# Output: "***0007****"
# Jawaban Anda:
id_num = "7"
# ...

print("=" * 50)

# ================================
# TODO 10: PRAKTEK REAL CASE
# ================================
# Soal: Diberikan list ID produk ["1", "12", "123", "1234"]
#       Format semua ID agar panjangnya 6 karakter dengan leading zero
#       Lalu cetak dalam kolom rata kanan dengan lebar 8 karakter
# Jawaban Anda:
ids = ["1", "12", "123", "1234"]
# ...

print("=" * 50)