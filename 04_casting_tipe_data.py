# casting artinya merubah dari satu tipe data ke tipe lain
# tipe data = int, float, str, bool

data_int = 0
print("data = ", data_int ,", type = ", type(data_int))

# mengubah tipe data INT
print("=========== INTEGER ===========")
data_float = float(data_int)
data_string = str(data_int)
data_boolean = bool(data_int) # akan false jika nilai = 0
print("data = ", data_float ,", type = ", type(data_float))
print("data = ", data_string ,", type = ", type(data_string))
print("data = ", data_boolean ,", type = ", type(data_boolean))

# mengubah tipe data BOOL

print("=========== BOOLEAN ===========")
data_bool = True
data_float = float(data_bool)
data_integer = int(data_bool) 
data_string = str(data_bool)
print("data = ", data_float ,", type = ", type(data_float))
print("data = ", data_string ,", type = ", type(data_string))
print("data = ", data_integer ,", type = ", type(data_integer))