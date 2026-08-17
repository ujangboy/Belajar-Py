print(f"masukan angka kurang dari \nangka 3 \natau \nlebih dari 10 ")

userInput = float(input(f"Masukan angka: "))

# kurang dari 3
kurangDari3 = userInput < 3
print(f"Hasil kurang dari 3: ", kurangDari3)

# lebih dari 10
lebihDari10 = userInput > 10
print(f"Hasil lebih dari 10: ", lebihDari10)

# hasil dari kduanya 
hasilCek = kurangDari3 or lebihDari10
print(f"angka yang kamu maksukan: ", hasilCek, (userInput))

print("\n", 10*"=")

# ------3+++++++10------
# irisan
print(f"masukan angka lebih dari \nangka 3 \natau \nkurang dari 10 \n")
userInput = float(input("\nmasukan angka: "))

#----- 3++++++
# lebih dari 3
lebihDari3 = userInput > 3
print(f"hasil lebih dari 3: ", lebihDari3)

# +++++++ 10 --------
# kurang dari 10
kurangdari10 = userInput < 10
print(f'hasil kurang dari 10: ', kurangdari10)

# ------3+++++++10------
hasikCek = lebihDari3 and kurangdari10
print(f"hasil angka kamu: ", hasilCek, (userInput))