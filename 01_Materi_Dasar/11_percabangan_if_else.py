# PERCABANGAN (CONTROL FLOW) - IF, ELIF, ELSE

# 1. If Inline (Ternary / Satu baris)
print("==== 1. TERNARY IF ====")
nama = "Budi"
print(f"Halo {nama}") if nama == "Budi" else print("Siapa kamu?")
hasil = "Bagus" if 10 > 5 else "Jelek"
print(f"Hasil: {hasil}\n")

# 2. If, Elif, Else Standard
print("==== 2. IF, ELIF, ELSE ====")
nilai = 75

if nilai >= 90:
    print("Predikat A: Luar biasa!")
elif nilai >= 80:
    print("Predikat B: Bagus sekali!")
elif nilai >= 70:
    print("Predikat C: Cukup baik")
else:
    print("Predikat D: Perlu banyak belajar lagi!")

# 3. Percabangan Bersarang (Nested If)
# If di dalam If
print("\n==== 3. NESTED IF (IF BERSARANG) ====")
umur = 20
punya_sim = True

if umur >= 17:
    print("Sudah cukup umur untuk mengemudi.")
    if punya_sim:
        print("Boleh mengemudi mobil karena punya SIM.")
    else:
        print("Tidak boleh mengemudi karena belum punya SIM.")
else:
    print("Belum cukup umur untuk mengemudi.")

# 4. If dengan Operator Logika Bersarang
print("\n==== 4. IF DENGAN LOGIKA ====")
user_role = "admin"
is_active = True

if user_role == "admin" and is_active:
    print("Akses ke Dashboard Admin Diberikan!")
elif user_role == "guest" or not is_active:
    print("Akses Terbatas: Mode Tamu atau Akun Nonaktif")
else:
    print("Akses Ditolak!")
