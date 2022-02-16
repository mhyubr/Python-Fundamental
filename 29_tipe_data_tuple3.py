import timeit

data_list = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]",number=10000000)
data_tuple = timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)",number=10000000)

print("waktu untuk memproses list :",data_list)
print("waktu untuk memproses tuple :",data_tuple)

# Data tuple lebih cepat untuk di olah karena 10 kali lebih cepat daripada lsit 