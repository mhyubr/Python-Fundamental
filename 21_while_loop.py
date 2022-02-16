# angka = int(input("masukkan angka : "))

# while angka < 5:
#     print('nilai angka adalah :',angka)
#     angka = angka + 1

# print('end of while')

# start = True # variabel boolean

# while start:
#     print("di dalam while")
#     if angka == 100:
#         start = False
#         print('angka 100 ditemukan')
#     angka += 1


# else, break, continue, pass

angka = 0 

while angka < 10:

    if angka is 5:
        angka += 1
        # print('checkpoint 1')
        break
        continue
        pass
        # print('checkpoint 2')

    print('nilai angka adalah',angka)
    angka += 1
else:
    print('nilai angka diakhir while',angka)

print('out of while')