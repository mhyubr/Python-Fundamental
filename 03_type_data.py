# a = 10, a adalah variabel dengan nilai 10

# tipe data : Angka satuan tanpa menggunakan koma / desimal (integer)
data_integer = 150
print("data : ", data_integer, ", bertipe : ", type(data_integer))

# tipe data : Angka dengan koma / desimal (float)
data_float = 1.5
print("data : ", data_float, ", bertipe : ", type(data_float))

# tipe data : kumpulan karakte (string)
data_string = "hello 10"
print("data : ", data_string, ", bertipe : ", type(data_string))

# tipe data : binner true/false atau 1/0 (boolean)
data_bool = True
print("data : ", data_bool, ", bertipe : ", type(data_bool))


## tipe data khusus

# bilangan kompleks
data_kompleks = complex(5,6)
print("data : ", data_kompleks, ", bertipe : ", type(data_kompleks))
# hasilnya (5+6j)    (j = imajiner)


## tipe data dari bahasa C

# karena python dibuat dari bahasa C jadi kita dapat
# menggunakan bahasa C di python
# dengan syarat meng-import package-nya

from ctypes import c_double, c_char, c_long

#tipe data double
data_c_double = c_double(10.5)
print("data : ", data_c_double, ", bertipe : ", type(data_c_double))