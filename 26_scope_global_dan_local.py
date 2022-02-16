# scope variabel : mengakses nilai global dalm variabel local

nama = 'muhammad'
makananKesukaan = 'coto'

def rubahNama(namaBaru):
    global nama
    nama = namaBaru # variabel global
    namaAku = namaBaru # variabel local
    print('nama saya adalah',namaAku)

def makan(makanan, namaSaya):
    global nama, makananKesukaan
    nama = namaSaya
    makananKesukaan = makanan

rubahNama('ayyub')
makan('sate','AYYUB')

print('nama saya',nama,'Saya suka makan', makananKesukaan) 