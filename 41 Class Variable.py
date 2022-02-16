# class
class mahasiswa():

    jurusan = "ekonomi"

    jumlah_mahasiswa = 0

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama
        self.nim = input_nim

        mahasiswa.jumlah_mahasiswa += 1

# main program
ayyub = mahasiswa("Muhammad Ayyub Ramli",1202201296)
otong = mahasiswa("Otong Surotong",1202201521)
cassandra = mahasiswa("Cassandra aja",1202203132)

mahasiswa.jurusan = "ekonomi mikro"
ayyub.jurusan = "ekonomi makro"
ayyub.kegemaran = "ngoding"

print(mahasiswa.jurusan)
print(ayyub.jurusan)
print(ayyub.kegemaran)
print(otong.jurusan)

print(mahasiswa.jumlah_mahasiswa)

# print(mahasiswa.__dict__)
# print(ayyub.__dict__)