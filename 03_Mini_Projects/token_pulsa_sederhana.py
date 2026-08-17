# membuat simulasi token pulsa
import random

class token:
    harga_perkoten = 26
    
    def __init__ (self, nama_pembeli, harga):
        self.harga = harga
        self.nama_pembeli = nama_pembeli
        self.token = self.random_token()
        self.kwh = self.perhitungan()
        
    def info(self):
        return f"pembelian =  atas nama:  {self.nama_pembeli},  dengan harga: {self.harga}, dengan KWH sebesar:  {self.kwh}" 
    
    def perhitungan(self):
        return round(self.harga / self.harga_perkoten, 2) # memkai round untuk membualatkan hasil pembagian dengan 2 angka dibelakang koma
    
    def format_token(self, raw_token):
        return '-'.join(raw_token[i:i+4] for i in range(0, len(raw_token), 4)) # menambahkan tanda - setiap 4 karakter pada hasil random toket 
    
    def random_token(self):
        raw = ''.join([str(random.randint(0,9)) for _ in range (20)])
        return self.format_token(raw)
    
    def struk_pembelian(self):
        
        return (
          
            f"\n === STRUK PEMBELIAN ===\n"
            f"nama pembeli: {self.nama_pembeli} \n"
            f"harga beli: {self.harga}\n"
            f"kwh: {self.kwh}\n"
            f"token: {self.token}\n"
        )
 
    
if __name__ == "__main__" : 
    print("=== SELAMAT DATANG DI TOKO PULSA ===")
    print(f"harga token {token.harga_perkoten} untuk pembelian token")
    print(f"minal pembelian = 10.000")
    nama_pembeli = (input("masukan nama pembeli: "))
while True:
    harga = int(input("masukan harga: "))
    
    if harga < 10000:
        print("peringatan: harga dibawah 10.000 saldo anda kurang")
    
    else:
        break
    
pembelian = token(nama_pembeli, harga)
print(pembelian.info())
print(pembelian.struk_pembelian())       

 
  