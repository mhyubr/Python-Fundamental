# List (datanya bisa diubah dan memiliki jenis data berbeda)
Ganjil = [1,3,5,7,9]

# Tuple (datanya fix tidak dapat diubah dan jenis data harus sama tetapi lebih ringan diproses daripada list)
Genap = (2,4,6,8,10)

print(type(Ganjil))
print(type(Genap))

Ganjil[2] = 99
# Genap[2] = 99

Ganjil.append(11)
# Genap.append(12)

Ganjil.remove(1)
# Genap.remove(2)

print(Ganjil)
print(Genap)

# Cetak operasi apa aja yang bisa dilakukan untuk tuple dan list
print(dir(Ganjil),"\n")
print(dir(Genap))