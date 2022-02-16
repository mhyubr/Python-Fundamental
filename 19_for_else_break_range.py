number = int(input('masukkan angka : '))

for i in range(0,40,5):
    print(i)
    if i is number:
        print('angka ditemukan',i)
        break
else:
     print('angka tidak ditemukan')

print("space di luar for")