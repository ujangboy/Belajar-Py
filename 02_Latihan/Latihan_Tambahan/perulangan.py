# perulangan if else
nama = "amelia" 

if nama == "amelia":
    print("nama saya amelia")
else:   print("nama saya bukan amelia")

print("\n", 10*"=")

# perulangan while

angka = 0

while angka < 5:
    print(f"angka: {angka}")
    angka += 1
    
print("\n", 10*"=")

# perulangan for
for i in range(8):
    print(f"angka: {i}")
    
print("\n", 10*"=")
# perulangan for dengan list
buah = ["apel", "jeruk", "mangga", "pisang"]
for i in buah:
    print(f"buah: {i}")
    
print("\n", 10*"=")

print("perulangan for dengan string")

string = "hello world"

for i in range(len(string)):
    print(f"karakter {i+1}: {string[i]}", )
    

  
