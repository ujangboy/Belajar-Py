# formating and leterals

#1 zfill(width) sama dengan zero nol
# maksudnya menambahkan angka no di depan angka angka atau kiri sampai panjang tertentu 
print("====================================")
print("Contoh zfill()")
angka = "42"
print(angka.zfill(5))  # Output: 00042

angka_negatif = "-420"
print(angka_negatif.zfill(5))  # Output: -0042 (tanda minus tetap di kiri)

#  Formatting angka: Untuk membuat nomor urut/kode yang konsisten (misal: 001, 002, 010)
# Kompatibilitas sistem: Banyak sistem (seperti database, file naming) butuh fixed-width numeric format
#Natural sorting: "file002" akan diurutkan benar setelah "file001" (tanpa zfill: "file10" muncul sebelum "file2")

#2 rjust(width, fillchar=' ') - Right Justify
# Menambahkan karakter (default spasi) di kiri string sampai panjang tertentu → teks "rata kanan".
print("====================================")
print("Contoh rjust()")
teks = "hai"
print(teks.rjust(10)) # Output: '       hai' (dengan 7 spasi di kiri)
print(teks.rjust(10, '-')) # Output: '-------hai' (dengan 7 tanda minus di kiri)

# Alignment teks: Untuk membuat tabel/kolom rapi di konsol
# Formatting output: Laporan keuangan, daftar harga, dll butuh rata kanan untuk angka
# Visual consistency: Membuat UI konsol terlihat terstruktur

#3 ljust(width, fillchar=' ') - Left Justify
# Menambahkan karakter (default spasi) di kanan string sampai panjang tertentu → teks "rata kiri".
print("====================================")
print("Contoh ljust()")
teks = "hai"
print(teks.ljust(10)) # Output: 'hai       ' (dengan 7 spasi di kanan)
print(teks.ljust(10, '-')) # Output: 'hai-------' (dengan 7 tanda minus di kanan)

# Default alignment: Teks biasanya dibaca rata kiri (natural untuk bahasa Latin)
# Kolom deskriptif: Label/keterangan biasanya rata kiri, nilai rata kanan
# Padding untuk alignment: Bersama rjust() membentuk tabel sederhana

#4 center(width, fillchar=' ')
# menambahkan karekter di kedua sisi string atau teks menjadi di tengah
print("====================================")
print("Contoh center()")
judul = "MENU"
print(judul.center(10)) # Output: '   hai    '
print(judul.center(20, "=")) # Output: '========MENU========'

# Highlighting text: Judul/header sering ditengah untuk menarik perhatian
# Balanced layouts: Membuat tampilan UI konsol lebih estetis
# UI konsol: Membuat antarmuka CLI terlihat profesion
#  Formatting dokumen: Untuk presentasi teks yang eye-catching

print("====================================")
print("macam macam-macam string literals pada pyrton")
# String Literals
single_quoted = 'Hello, World!'                 # Default, praktis jika ada " di dalam string
double_quoted = "Hello, World!"                 # Praktis jika ada ' di dalam string
triple_single_quoted = '''Hello'''              # Untuk string multi-baris atau yang mengandung ' dan "
triple_double_quoted = """Hello, World!"""      # Multiline + docstring 
f_string = f"Hello, {'World'}!"                 # String pada py v 3.6+, untuk interpolasi variabel
raw_string = r"C:\new_folder\test.txt"          # Mengabaikan escape sequences
print(single_quoted)
print(double_quoted)
print(triple_single_quoted)
print(triple_double_quoted)
print(f_string)
print(raw_string)
# Fleksibilitas: Hindari escaping berlebihan (\", \')
# Readability: Kode lebih mudah dibaca
# Special use cases: Multiline, formatting, path Windows, regex

print("====================================")
print("contoh raw string")
#6 Raw String (r"...") - Escape Sequence Dimatikan
# String yang mengabaikan backslash \ sebagai escape character.

print("tanpa raw string: ")
# kemungkinan tanpa r akan terjadi error atau output tidak sesuai harapan
path = "C:\new\forder"
print(path)  # Output mungkin tidak sesuai harapan karena \n dianggap newline

print("dengan raw string: ")
# dengan raw string
raw_path = r"C:\new\forder"
print(raw_path)  # Output: C:\new\forder 

# contoh untuk regex
pattern = r"\d{3}-\d{4}" # tanpa r, harus "\\d{3}-\\d{4}" 
print("Pattern regex:", pattern)  # Output: \d{3}-\d{4}

# Path Windows: Backslash \ adalah separator path di Windows
# **Regular expression**: Regex penuh dengan \d, \w, \s yang butuh escaping
# **Avoid double escaping**: Tanpa r, harus tulis \\ untuk setiap \ → kode jadi messy


print("\n====================================")
""""
1. zfill()
untuk tujuan : Numeric alignment
analogi: Nomor antrian RS: 001, 002, ... 100

2. rjust()
untuk tujuan: Numeric formatting
analogi: Kolom harga di struk: angka rata kanan

3. ljust()
untuk tujuan: Text alignment
analogi: Label produk di rak: nama rata kiri

4. center()
untuk tujuan: Visual emphasis
analogi: Judul buku di sampul: ditengahkan 

5. String literals
untuk tujuan: Code readability
analogi: Pilih tanda kutip sesuai konten

6. Raw string
untuk tujuan: Literal backslash
anlogi: Menulis alamat jalan tanpa "terjemahan"""

# membuat contoh paktrik 
print("contoh contoh")


