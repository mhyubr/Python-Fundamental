# class (harus di atas / karena python interprate languahe)

class mahasiswa():
    nama = 'nama' # atribut atau nilai yang menempel di dalam class

    def belajar(self, kondisi) : # method atau fungsi yang menempel di dalam class
        print(self.nama,'saya belajar',kondisi)

    def tidur(self): # method atau fungsi yang menempel di dalam class
        print(self.nama,'tidur di kelas')

# main program

ayyub = mahasiswa()
otong = mahasiswa()

ayyub.nama = 'Muhammad Ayyub Ramli'
otong.nama = 'michael otong'

print(ayyub.nama)
print(otong.nama)

ayyub.belajar('dengan giat') # method
otong.tidur() # method
