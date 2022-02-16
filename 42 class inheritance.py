# class
class Ojek(): # class parent

    def __init__(self,nama,transmisi,daerah_kerja):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah_kerja = daerah_kerja

    def cekID(self):
        print('nama\t:',self.nama,'\nmotor\t:',self.transmisi,"\ndaerah\t:",self.daerah_kerja,"\n")

# Prinsip programer jangan melakukan DRY (Don't Repeat Yourself)
# Makanya digunakan Inheritance

class Gojek(Ojek): # class child
    pass # class kosong

class Grab(Ojek):
    def cekID(self):
        print('cek aplikasi Grab\n')

# main program
ojek1 = Ojek('Mario','Manual','Bandung Selatan')
ojek2 = Gojek('Jackson','Automatic','Tasikmalaya')
ojek3 = Grab('Michael','Automatic','Makassar')

ojek1.cekID()
ojek2.cekID()
ojek3.cekID()