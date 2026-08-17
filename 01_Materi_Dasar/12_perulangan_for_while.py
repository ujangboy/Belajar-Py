# PERULANGAN (LOOPING) - FOR & WHILE

# 1. FOR LOOP
print("==== 1. FOR LOOP (Perulangan For) ====")

# Looping menggunakan list
angka_list = [1, 2, 3, 4, 5]
for i in angka_list:
    print(f"Iterasi list ke-{i}")

# Looping menggunakan range
# range(start, stop, step)
print("\nMenggunakan Range:")
for i in range(1, 6): # akan loop dari 1 s/d 5
    print(f"Angka: {i}")

# Looping menggunakan string
print("\nMenggunakan String:")
for huruf in "PYTHON":
    print(huruf)


# 2. WHILE LOOP
print("\n==== 2. WHILE LOOP (Perulangan While) ====")
# Perulangan yang bergantung pada suatu kondisi true/false
angka = 1
while angka <= 3:
    print(f"While Loop angka {angka}")
    angka += 1 # IMPORTANT: Jangan lupa di increment agar tidak infinite loop


# 3. PERULANGAN BERSARANG (NESTED LOOP)
print("\n==== 3. NESTED LOOP (Perulangan Bersarang) ====")
# Contoh membuat kotak bintang (Matrix)
baris = 3
kolom = 4
for i in range(baris):
    baris_bintang = ""
    for j in range(kolom):
        baris_bintang += "* "
    print(baris_bintang)


# 4. CONTROL STATEMENT (BREAK, CONTINUE, PASS)
print("\n==== 4. BREAK, CONTINUE, PASS ====")

# BREAK (Menghentikan perulangan sepenuhnya)
print("Contoh BREAK:")
for i in range(1, 10):
    if i == 5:
        print("Break pada angka 5, perulangan berhenti!")
        break
    print(f"Angka {i}")

# CONTINUE (Melompati iterasi saat ini dan lanjut ke iterasi berikutnya)
print("\nContoh CONTINUE:")
for i in range(1, 6):
    if i == 3:
        print("Continue pada angka 3, melompat ke angka berikutnya!")
        continue
    print(f"Angka {i}")

# PASS (Tidak melakukan apa-apa, berfungsi sebagai placeholder dummy)
print("\nContoh PASS:")
for i in range(1, 3):
    pass # Dummy block, tidak error karena pass
print("Perulangan pass selesai tanpa melakukan apa-apa.")
