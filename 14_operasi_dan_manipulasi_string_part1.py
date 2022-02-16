# operasi dan maninpulasi string

# 1. menyambung string (concatenate)
nama_pertama = "Muh"
nama_tengah = "Ayyub"
nama_akhir  = "Ramli"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print('panjang dari "' + nama_lengkap + '" = ' + str(panjang))

# 3. operator untuk string

# mengecek apakah ada komponen char atau string di string
r = "r"
status = r in nama_lengkap
print("string " + r + " ada di " + nama_lengkap + " " + str(status))
r = "R"
status = r in nama_lengkap
print("string " + r + " ada di " + nama_lengkap + " " + str(status))

# mengulang string
print("wk"*10)
print(15*"wk")

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-1 : " + nama_lengkap[1])
print("index ke-2 : " + nama_lengkap[2])
print("index ke-3 : " + nama_lengkap[3])
print("index ke-4 : " + nama_lengkap[4])
print("index ke-5 : " + nama_lengkap[5])
print("index ke-6 : " + nama_lengkap[6])
print("index ke-7 : " + nama_lengkap[7])
print("index ke-8 : " + nama_lengkap[8])
print("index ke-9 : " + nama_lengkap[9])
print("index ke-10 : " + nama_lengkap[10])
print("index ke-11 : " + nama_lengkap[11])
print("index ke-12 : " + nama_lengkap[12])
print("index ke-13 : " + nama_lengkap[13])
print("index ke-14 : " + nama_lengkap[14])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-2) : " + nama_lengkap[-2])
 # untuk 4 sampai 8ditambah 1 jadi [4:9]
print("index ke-(4 sampai 8) : " + nama_lengkap[4:9])
# kelipatan 2
print("index ke-(0 sampai 15) : " + nama_lengkap[0:16:2])

# item paling kecil (paling sedikit muncul)
print("paling kecil : " + min(nama_lengkap))

# item paling besar (paling banyak muncul)
print("paling besar : " + max(nama_lengkap))

# ASCII code
ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# 4. operator dalam bentuk method

data = "Muhammad Ayyub Ramli"
jumlah = data.count("y")
print("jumlah y pada " + data + " = " + str(jumlah))