import sys

data_list = [1,2,3,4,5,"pisang goreng","natasha wilona", False, True, 3.14]
data_tuple = (1,2,3,4,5,"pisang goreng","natasha wilona", False, True, 3.14)

besar_datalist = sys.getsizeof(data_list)
besar_datatuple = sys.getsizeof(data_tuple)

print("Besar data list:", besar_datalist)
print("Besar data tuple:", besar_datatuple)

# Memori yang digunakan tuple lebih kecil karena tuple hanya terdiri dari beberapa operasi
# Ini berguna untuk data yang relatif banyak atau besar