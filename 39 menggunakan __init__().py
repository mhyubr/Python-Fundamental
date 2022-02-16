class mahasiswa():
    # nama = 'nama'

    # akan dijalankan pertama kali ketika class mahasiswa() di panggil
    def __init__(self, input_nama, input_nim):
        # print("ini adalah init")
        self.nama = input_nama
        self.nim = input_nim

    def belajar(self,kondisi):
        print(self.nama,'sedang belajar',kondisi)

    def tidur(self):
        print(self.nama,'tidur di kelas')

ayyub = mahasiswa("Muhammad Ayyub Ramli",1202201296)
# otong = mahasiswa()

print(ayyub.nama)
print(ayyub.nim)

ayyub.belajar("dengan giat")

# ayyub.nama = "Muhammad Ayyub Ramli"
# ayyub.nama = "Michael Otong"