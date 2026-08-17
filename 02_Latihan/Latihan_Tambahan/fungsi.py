# fungsi

def tambah(a, b):
    return a + b

print(tambah(2, 3))  # Output: 5    

# contoh fungsi dengan parameter default
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())  # Output: Hello, Guest!
print(greet("Alice"))  # Output: Hello, Alice!

# contoh fungsi dengan parameter variabel
def jumlahkan_semua(*args): # args adalah parameter variabel yang dapat menerima sejumlah argumen
    print(f"menirima angka: {args}")
    return sum(args)

print(jumlahkan_semua(1,2,3,4,5)) # Output: 15
print(jumlahkan_semua(10, 20)) # Output: 30

print("\n", 10*"=")
# contoh fungsi dengan parameter keyword
def introduce(**kwargs): # kwargs adalah parameter keyword yang dapat menerima sejumlah argumen dengan nama
    return ", ".join(f"{key}: {value}" for key, value in kwargs.items())

print(introduce(name="Alice", age=30, city="New York"))  # Output: name: Alice, age: 30, city: New York

print("\n", 10*"=")

# agrs dalam string 
def format_string(nama, umur):
    return f"nama saya {nama} dan umur saya {umur} tahun"

print(format_string("amelia", 25))  # Output: nama saya amelia dan umur saya 25 tahun
print(format_string(umur=30, nama="bob"))  # Output: nama saya bob dan umur saya 30 tahun