# membuat simulasi toket pulsa
import random

class token:
    harga__perkoten = 26
    
    def __init__ (self, nama_pembeli, harga):
        self.harga = harga
        self.nama_pembeli = nama_pembeli
        self.token = self.random_token
        self.kwh = 0.0
    def info(self):
        return (f"pembelian = " "atas nama ", {self.nama_pembeli},  {self.harga}, "dengan " ,{self.kwh} )
    
    def perhitungan(self):
        return (self.harga / self.harga__perkoten)
    
    def random_token(self):
        return ''.join([str(random.randint(0,9)) for _ in range (20)])
    
    def struk_pembelian(self):
        
        return (
            f"'='*20\n "
            f"' === STRUK PEMBELIAN ===\n"
            f"nama pembeli: , {self.nama_pembeli}"
            f"harga beli: , {self.harga}"
            f"kwh: ,{self.kwh}"
            f"token: , {self.token}"
        )
def menu_utama(self):      

 pembeli = input(f"masukan nama: , {self.nama_pembeli}")
 token = input(f"masukan harga: , {self.harga}")
 
    
if __name__ == "__main__" : 
    struk_pembelian:
        
  