# set / himpunan :
# tidak punya urutan

superhero = {"wiro sableng", "si buta dari gua hantu", "saras 008", "gundala", "gatot kaca"}

superhero.add("mak lampir")
superhero.add("gundala")
print(superhero)

nilai = set()

nilai.add("sepuluh")
nilai.add(10)
nilai.add("sembilan koma lima")
nilai.add(9.5)

print(nilai)

ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {2,3,5,7}

# gabungan himpunan
print(ganjil.union(genap))

# irisan himpunan
print(ganjil.intersection(genap))
print(ganjil.intersection(prima))