# REGULAR EXPRESSION (RE)

import re

# 1. FUNGSI DASAR RE
print("==== 1. FUNGSI DASAR RE ====")

teks = "Hari ini saya makan 3 apel dan 4 jeruk. HP: 0812-3456-7890"

# re.search() - cari pattern pertama yang cocok
hasil = re.search(r"\d+", teks)
if hasil:
    print(f"Angka pertama: {hasil.group()}")

# re.findall() - cari semua pattern yang cocok (list)
angka = re.findall(r"\d+", teks)
print(f"Semua angka: {angka}")

# re.match() - cek di AWAL string saja
hasil = re.match(r"Hari", teks)
print(f"Match di awal: {hasil.group() if hasil else 'Tidak cocok'}")

# re.finditer() - iterator dari semua match
print("\nSemua match dengan posisi:")
for match in re.finditer(r"\d+", teks):
    print(f"  '{match.group()}' di posisi {match.start()}-{match.end()}")

# 2. METAKARAKTER UMUM
print("\n==== 2. METAKARAKTER ====")

teks2 = "abc123_def-456 ghi"

# \d = digit (0-9)
print(f"Digit: {re.findall(r'\d', teks2)}")

# \D = non-digit
print(f"Non-digit: {re.findall(r'\D', teks2)}")

# \w = word character (a-z, A-Z, 0-9, _)
print(f"Word char: {re.findall(r'\w', teks2)}")

# \W = non-word char
print(f"Non-word: {re.findall(r'\W', teks2)}")

# \s = whitespace (spasi, tab, newline)
print(f"Whitespace: {re.findall(r'\s', teks2)}")

# \S = non-whitespace
print(f"Non-whitespace: {re.findall(r'\S', teks2)}")

# . (dot) = kecuali newline (seluruh kecuali enter)
print(f"Dot all: {re.findall(r'.', teks2)}")

# ^ = mulai string, $ = akhir string
print(f"Awal 'abc': {bool(re.search(r'^abc', teks2))}")
print(f"Awal 'xyz': {bool(re.search(r'^xyz', teks2))}")

# 3. QUANTIFIER (KUANTIFIKASI)
print("\n==== 3. QUANTIFIER ====")

teks3 = "aa aaa aaaa aaaaa"

# * = 0 atau lebih
print(f"a* (nol+): {re.findall(r'a*', teks3)}")

# + = 1 atau lebih
print(f"a+ (satu+): {re.findall(r'a+', teks3)}")

# ? = 0 atau 1 (opsional)
print(f"a? (nol/satu): {re.findall(r'a?', teks3)}")

# {n} = tepat n kali
print(f"a{{3}}: {re.findall(r'a{3}', teks3)}")

# {n,m} = antara n sampai m kali
print(f"a{{2,4}}: {re.findall(r'a{2,4}', teks3)}")

# 4. CHARACTER CLASS
print("\n==== 4. CHARACTER CLASS ====")

teks4 = "apple, banana, cherry, date"

# [abc] = salah satu dari a, b, atau c
print(f"[abc]+: {re.findall(r'[abc]+', teks4)}")

# [a-z] = huruf kecil, [A-Z] = huruf besar, [0-9] = angka
print(f"Kata dimulai [a-z]+: {re.findall(r'[a-z]+', teks4)}")

# [^abc] = KECUALI a, b, c (^ di dalam [] berarti NOT)
print(f"Bukan a/d/b: {re.findall(r'[^a]c\w+', teks4)}")

# 5. GROUPING DAN CAPTURE
print("\n==== 5. GROUPING ====")

email = "Email saya adalah andi@example.com dan budi@test.org"
pattern = r"([a-zA-Z0-9]+)@([a-zA-Z0-9]+\.[a-zA-Z]+)"

matches = re.finditer(pattern, email)
for m in matches:
    print(f"  Full: {m.group(0)}")
    print(f"  User: {m.group(1)}")
    print(f"  Domain: {m.group(2)}")

# 6. RE.SUB (SUBSTITUTION)
print("\n==== 6. RE.SUB ====")

teks5 = "Harga: 10000, Diskon: 2000, Total: 8000"
# Ganti semua angka dengan 'X'
hasil = re.sub(r"\d+", "X", teks5)
print(f"Asli: {teks5}")
print(f"Ganti angka: {hasil}")

# Hapus semua non-digit
hanya_angka = re.sub(r"\D", "", teks5)
print(f"Hanya angka: {hanya_angka}")

# 7. FLAGS (OPSIONAL)
print("\n==== 7. FLAGS ====")

teks6 = "Hello World\nhello universe"

# re.IGNORECASE (re.I) = tidak peduli huruf besar/kecil
print(f"Case insensitive: {re.findall(r'hello', teks6, re.IGNORECASE)}")

# re.MULTILINE (re.M) = ^ dan $ berlaku per baris
print(f"Multiline: {re.findall(r'^hello', teks6, re.MULTILINE)}")
