# operator dalam bentuk methods

## merubah case dari string

# merubah semua ke upper case
salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case
alay= "aKu KeCe AbieeeezZZZZZZZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan isX method

# contoh pengecekan lower cas
salam = "sist"
apakah_lower = salam.islower() 
# penambahan is untuk  pengecekan  (hasilnya bool)
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() 
# penambahan is untuk  pengecekan  (hasilnya bool)
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- untuk mengecek huruf dan angka
# isspace() <-- untuk mengecek angka saja
# ispace() <-- untuk mengecek spasi, tab, newlin \n
# istitle() <-- untuk mengecek semua kata dimulai dengan huruf besar

judul = "Im done"
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul))
judul = "Im Done"
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul))
judul = "I'm Done"
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul))

# mengecek komponen startwith() endswith() <-- keren
cek_start = "Sanjangnim Oppa".startswith("Sanjangnim")
print("start = " + str(cek_start))
# mengecek komponen startwith() endswith() <-- keren
cek_end = "Sanjangnim Oppa".endswith("Oppa")
print("end = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabung = ','.join(pisah)
print(gabung)
gabung = ' '.join(pisah)
print(gabung)
gabung = ' ehm '.join(pisah)
print(gabung)
gabung = "akuehmsayangehmkamu"
print(gabung.split('ehm'))


## alokasi karakter rjust() ljust() center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")
kiri = "kiri".ljust(10)
print("'"+kiri+"'")
tengah = "tengah".center(20,":")
print("'"+tengah+"'")
# kebalikannya -> strip ()
tengah = tengah.strip(":") # menghilangkan tanda :
print("'"+tengah+"'")
kanan = kanan.strip(" ") # menghilanhkan spasi
print("'"+kanan+"'")