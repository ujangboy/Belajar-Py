"""
QUIZ PYTHON - MINGGU (SUNDAY)
Topik: Kombinasi Semua Konsep (Mini Projects)
Difficulty: Advanced
"""

print("=" * 60)
print("PYTHON QUIZ - MINGGU (SUNDAY)")
print("Kombinasi Semua Konsep: Variables, Loops, Functions, Dictionary")
print("=" * 60)
print()

# ============================================
# PROJECT 1: Sistem Manajemen Nilai Siswa
# ============================================

print("PROJECT 1: Sistem Manajemen Nilai Siswa")
print("-" * 60)

def tambah_siswa(data_siswa, nama, nilai):
    """Menambah siswa baru"""
    data_siswa[nama] = nilai
    return data_siswa

def hitung_statistik(data_siswa):
    """Menghitung statistik nilai"""
    if not data_siswa:
        return None
    
    nilai_list = list(data_siswa.values())
    return {
        "rata_rata": sum(nilai_list) / len(nilai_list),
        "tertinggi": max(nilai_list),
        "terendah": min(nilai_list),
        "jumlah_siswa": len(data_siswa)
    }

# Data siswa
siswa_data = {}
siswa_data = tambah_siswa(siswa_data, "Adi", 85)
siswa_data = tambah_siswa(siswa_data, "Budi", 90)
siswa_data = tambah_siswa(siswa_data, "Citra", 78)
siswa_data = tambah_siswa(siswa_data, "Dina", 92)
siswa_data = tambah_siswa(siswa_data, "Eka", 88)

print("Data Siswa:")
for nama, nilai in siswa_data.items():
    print(f"  {nama}: {nilai}")

stats = hitung_statistik(siswa_data)
print(f"\nStatistik Nilai:")
print(f"  Rata-rata: {stats['rata_rata']:.1f}")
print(f"  Nilai Tertinggi: {stats['tertinggi']}")
print(f"  Nilai Terendah: {stats['terendah']}")
print(f"  Jumlah Siswa: {stats['jumlah_siswa']}")
print()

# ============================================
# PROJECT 2: Kalkulator Belanja Toko
# ============================================

print("PROJECT 2: Kalkulator Belanja Toko")
print("-" * 60)

def proses_belanja(items, harga_items):
    """
    Memproses belanja dengan perhitungan:
    - Total harga
    - Diskon (jika total > 500000, diskon 10%)
    - Total pembayaran
    """
    total = 0
    
    print("Detail Belanja:")
    for i, item in enumerate(items):
        subtotal = item * harga_items[i]
        total += subtotal
        print(f"  {i+1}. {harga_items[i]} x {item} = Rp{subtotal:,}")
    
    diskon = 0
    if total > 500000:
        diskon = total * 0.1
    
    total_akhir = total - diskon
    
    print(f"\nSubtotal: Rp{total:,}")
    print(f"Diskon (10%): Rp{diskon:,.0f}")
    print(f"Total Bayar: Rp{total_akhir:,.0f}")
    
    return total_akhir

# Data belanja
belanja_items = [2, 1, 3]  # qty
harga_items = [50000, 150000, 75000]  # harga per item
proses_belanja(belanja_items, harga_items)
print()

# ============================================
# PROJECT 3: Validasi dan Manipulasi Data
# ============================================

print("PROJECT 3: Validasi dan Manipulasi Data")
print("-" * 60)

def validasi_email(email):
    """Validasi format email"""
    return "@" in email and "." in email

def validasi_nomor_telepon(nomor):
    """Validasi nomor telepon"""
    return len(nomor) >= 10 and nomor.isdigit()

def buat_username(nama):
    """Membuat username dari nama"""
    nama_lower = nama.lower()
    username = nama_lower.replace(" ", "_")
    return username

# Test validasi
data_user = {
    "nama": "Andi Kurniawan",
    "email": "andi@example.com",
    "telepon": "08123456789"
}

print("Validasi Data User:")
print(f"  Nama: {data_user['nama']}")
print(f"  Email valid? {validasi_email(data_user['email'])}")
print(f"  Telepon valid? {validasi_nomor_telepon(data_user['telepon'])}")
print(f"  Username: {buat_username(data_user['nama'])}")
print()

# ============================================
# PROJECT 4: Deret Bilangan dan Pola
# ============================================

print("PROJECT 4: Deret Bilangan dan Pola")
print("-" * 60)

def deret_aritmatika(a, b, n):
    """Membuat deret aritmatika"""
    deret = []
    for i in range(n):
        deret.append(a + (i * b))
    return deret

def pola_segitiga_angka(n):
    """Membuat pola segitiga dengan angka"""
    pola = ""
    for i in range(1, n + 1):
        pola += " ".join(str(j) for j in range(1, i + 1)) + "\n"
    return pola

# Deret Aritmatika
print("Deret Aritmatika (a=2, b=3, n=10):")
deret = deret_aritmatika(2, 3, 10)
print(f"  {deret}")

# Pola Segitiga
print("\nPola Segitiga Angka (n=5):")
print(pola_segitiga_angka(5))

# ============================================
# PROJECT 5: Game Tebak Angka
# ============================================

print("PROJECT 5: Game Tebak Angka (Simulasi)")
print("-" * 60)

def main_game():
    """Main game tebak angka"""
    import random
    
    angka_rahasia = random.randint(1, 100)
    kesempatan = 5
    tebakan = 0
    
    print(f"Permainan Tebak Angka (1-100)")
    print(f"Kesempatan: {kesempatan} kali\n")
    
    # Simulasi 3 tebakan
    tebakan_list = [45, 75, 82]
    
    for tebak in tebakan_list:
        kesempatan -= 1
        if tebak == angka_rahasia:
            print(f"Tebakan Anda: {tebak} ✓ BENAR!")
            return True
        elif tebak < angka_rahasia:
            print(f"Tebakan Anda: {tebak} - Terlalu kecil")
        else:
            print(f"Tebakan Anda: {tebak} - Terlalu besar")
        print(f"Kesempatan tersisa: {kesempatan}\n")
    
    print(f"Game Over! Angka yang benar adalah: {angka_rahasia}")
    return False

main_game()
print()

# ============================================
# PROJECT 6: Text Analysis
# ============================================

print("PROJECT 6: Text Analysis")
print("-" * 60)

def analisis_teks(teks):
    """Menganalisis teks"""
    return {
        "jumlah_karakter": len(teks),
        "jumlah_kata": len(teks.split()),
        "jumlah_huruf_a": teks.lower().count('a'),
        "teks_reversed": teks[::-1],
        "teks_uppercase": teks.upper(),
        "teks_title": teks.title()
    }

teks = "Python adalah bahasa pemrograman yang powerful"
analisis = analisis_teks(teks)

print(f"Teks: {teks}\n")
print("Analisis:")
for key, value in analisis.items():
    if key != "teks_reversed":
        print(f"  {key}: {value}")
print()

# ============================================
# PROJECT 7: Sistem Nilai Siswa Lengkap
# ============================================

print("PROJECT 7: Sistem Nilai Siswa (Dengan Grade)")
print("-" * 60)

def tentukan_grade(nilai):
    """Tentukan grade berdasarkan nilai"""
    if nilai >= 85:
        return "A"
    elif nilai >= 75:
        return "B"
    elif nilai >= 65:
        return "C"
    elif nilai >= 55:
        return "D"
    else:
        return "F"

# Data siswa dengan grade
siswa_values = {
    "Adi": 92,
    "Budi": 78,
    "Citra": 85,
    "Dina": 88,
    "Eka": 72
}

print("Daftar Nilai Siswa dengan Grade:")
print(f"{'Nama':<10} {'Nilai':<8} {'Grade':<6}")
print("-" * 24)
for nama, nilai in siswa_values.items():
    grade = tentukan_grade(nilai)
    print(f"{nama:<10} {nilai:<8} {grade:<6}")
print()

print("=" * 60)
print("QUIZ MINGGU SELESAI - SEMUA KONSEP DIKUASAI!")
print("=" * 60)
