class hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
        
    def info(self):
        return f"{self.nama} adalah jenis {self.jenis}"
  
  # membuat kelasa anak beruang dengan karekterristik bulu tebal dan memakan ikan  
class beruang_kutup(hewan):
        def __init__(self, nama, jenis, bulu, makanan): 
            super().__init__(nama, jenis)
            self.bulu = bulu
            self.makanan = makanan
        def info(self):
            return f"{self.nama} adalah jenis {self.jenis}, memiliki bulu yang {self.bulu}, dan makanannya adalah {self.makanan}"   
        

class badak(hewan):
        def __init__(self, nama, jenis, ukuran, makanan): 
            super().__init__(nama, jenis)
            self.ukuran = ukuran
            self.makanan = makanan
        def info(self):
            return f"{self.nama} adalah jenis {self.jenis}, dan memiliki ukuran yang {self.ukuran} makanan favoritnya adalah {self.makanan}"      
             
mamalia = beruang_kutup("beruang kutup", "mamalia", "tebal", "ikan")
mamalia_2 = badak("badak", "mamalia", "besar", "rumput")
print(mamalia.info())
print(mamalia_2.info())

"""
__init__ adalah kontrukteor yang menyimpan atribut nama dan jenis
(self, nama, jenis): parameter yang digunakan untuk menginisialisasi atribut nama dan jenis pada objek yang dibuat dari kelas hewan.
self di analogikan seperi box yang menyimpan atribut nama dan jenis 
self.nama = nama  untuk mnuoimpan nilai yang nantikan diberikan 
self.jenis = jenis

super()__ init__(nama, jenis) utuk mengangggil kontruktor yanga da di kelas induk


kenpaa lass beruang_kutup(hewan):
        def __init__(self, nama, jenis, bulu, makanan): ini di pangggil lagi? 
        karena karena kelas anak adalah atribut juga dari kelas hewan yang memiliki atribut jenis dan nama

"""
