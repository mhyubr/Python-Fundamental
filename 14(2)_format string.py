# FORMAT STRING

# contoh generic
nama = 'ucup'
hai = 'hello' + nama + ', apa kabar'
print(hai)

# string
format_str = f"hello {nama}"
print(format_str)

# boolean
boolean = True
format_str = f'{boolean}'
print(format_str)

# angka
angka = 2005.5
# format_str = 'angka =' + str(angka) # ribet
format_str = f'angka angka = {angka}' # mudah
print(format_str)

# bilangan bulat
angka = 15
format_str = f'bilangan bulat = {angka:d}'
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000
format_str = f'ribuan = {angka:,}'
print(format_str)

# bilangan dengan ordo jutaan
angka = 2000000
format_str = f'ribuan = {angka:,}'
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f'desimal = {angka:.2f}' # 2 angka dibelakang koma
format_str2 = f'desimal = {angka:.3f}' # 2 angka dibelakang koma
print(format_str)
print(format_str2)

# menampilkan leading zero
angka = 2005.54321
format_str = f'desimal = {angka:9.3f}' # akan membaca 9 angka
format_str2 = f'desimal = {angka:09.3f}' # angka yang kosong diganti 0
format_str3 = f'desimal = {angka:010.3f}' # angka yang kosong diganti 0
print(format_str)
print(format_str2)
print(format_str3)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10.25
format_minus = f'minus = {angka_minus:+d}' # + = plus negatif, d = integer
format_plus = f'plus = {angka_plus:+f}' # + = plus negatif, f = float
print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f'persen = {persentase:.2%}' # % untuk persen, . untuk angka dibelakang koma
print(format_persen)

# melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5
format_string = f'harga total = Rp.{harga*jumlah:,}'
print(format_string)

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f'binary = {bin(angka)}'
format_octal = f'octal = {oct(angka)}'
format_hexadecimal = f'hexadecimal = {hex(angka)}'
print(format_binary)
print(format_octal)
print(format_hexadecimal)