# fungsi dengan menggunakan argumen sederhana
def siswa(nama):
    print('siswa ini bernama',nama)

siswa('mario')

# fungsi dengan menggunakan keyword arguments

def guru(nama, pelajaran):
    print('guru ini bernama :',nama)
    print('mengajar pelajaran :',pelajaran)

guru(nama = 'popong', pelajaran='senirupa')
guru(pelajaran='olahraga',nama='endang')
guru('popong','senirupa')
guru('olahraga','endang') # imi contoh yang salah

# fungsi dengan engunakan default arguments

def penjagaSekolah(nama,shift='siang',sifat='lembut'):
    print("penjaga sekolah ini bernama :",nama)
    print('shiftnya :',shift)
    print('sifat :',sifat)

penjagaSekolah('Entis')
penjagaSekolah('Maman',shift='malam')
penjagaSekolah('Asep',sifat='Galak')