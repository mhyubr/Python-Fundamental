# input output file

# membuat file text

"""
w = write mode / mode menulis dan menghapus file lama, jika file tidak ada maka akan dibuat file baru
r = read mode only / hanya bisa baca
a = appending mode / menambahkan data di akhir baris
r+ = write and read mode
"""

file = open("file.txt","w")

file.write("ini adalah data text yang dibuat menggunakan python")
# setelah open jangan lupa close supaya filenya tertutup dan tersave otomatis
# input output file
'''
mode I/O:
w = write mode / mode menulis dan menghapus file lama
r = read mode only / hanya bisa baca
a = appendig mode / menambahkan data di akhir baris
r+ = write and read mode
'''

# membuat file text
file = open('data.txt', 'w')
file.write('ini adalah data text yang dibuat dengan menggunakan python')
file.write('\nini baris ke-2')
file.write('\nini baris ke-3')
file.write('\nini baris ke-4')
file.close() # wajib di close agar file tetap tersave karena text berjalan di ram python

# membaca file text
file2 = open('data.txt','r')
print(file2.read(10)) # membaca 10 karakter
print(file2.readline()) # membaca 1 baris
print(file2.read()) 
file2.close()

# appending mode
file3 = open('data.txt','a')
file3.write("\nbaris ini dibuat dengan menggunakan mode append")
file3.close()