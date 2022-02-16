# class
class mahasiswa():
   
    jurusan = "teknik tata boga" # public
    __nilai = 0 # private (nilai default)
    def __init__(self, input_nama, input_nim):
        self.nama = input_nama # public
        self.nim = input_nim # public

    def uts(self, input_nilai):
        self.__nilai += input_nilai
    
    def uas(self, input_nilai):
        self.__nilai += input_nilai
    
    def checkStatus(self):
        if self.__nilai <= 50:
            print(self.nama,'tidak lulus')
        else:
            print(self.nama,'lulus ')


# main program
ayyub = mahasiswa("Muhammad Ayyub Ramli",1202201296)
otong = mahasiswa("Otong Surotong",1202201521)

ayyub.uts(40)
ayyub.uas(100)

otong.uts(10)
otong.uas(30)

ayyub.checkStatus()
otong.checkStatus()

# print(ayyub.__nilai) # tidak dapat tercetak karena di private
# print(otong.__nilai) # tidak dapat tercetak karena di private