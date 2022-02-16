Barang = ['sepatu','ember','jaket','mobil']
print(Barang)

# beberapa method yang bisa digunakan untuk memanipulasi list

#method untuk menambah data kedalam list
Barang.append('sepeda')
print(Barang)

Barang.extend('dompet')
print(Barang)

Barang.insert(3,'sepatu')
print(Barang)

# method untuk menghitung anggota
jumlahSepatu = Barang.count('sepatu')
print('jumlah sepatu adalah',jumlahSepatu)

# meremove data
Barang.remove('sepatu')
print(Barang)

# membalik posisi list
Barang.reverse()
print(Barang)

# memmbuat list baru
print('='*90)
alatKantor = Barang.copy()
alatKantor.append('gelas')
print(alatKantor)
print(Barang)