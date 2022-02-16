# # error runtime (apabila format input salah)
# print = int(input("masukan angka sembarang?\n"))
# # error yang dapat dideteksi langsung oleh ide python (cth: visual studio code, pycharm, dll)
# print(nama saya mamat)

# def pembagian(a,b):
#     return a/b
# pembilang = int(input("masukkan angka pembilang:\n"))
# penyebut = int(input("masukkan angka penyebut:\n"))
# print(pembagian(pembilang,penyebut))

'''
ERROR HANDLING
'''
# try:
#     a = 1/0
# except:
#     print("error pembagian nol")
# print("akhir dari program")

while True:
    try:
        angka1 = int(input("Masukkan angka penyebut: "))
        angka2 = int(input("Masukkan angka pembilang: "))
        hasil = angka1/angka2
        break
    # except ValueError:
    #     print("yang anda masukkan bukan angka")
    # except ZeroDivisionError:
    #     print("angka penyebut tidak boleh 0")
    except Exception as err:
        print(err) # simple exception (tetapi berbahasa inggris)
        '''
        type of exception errors:
        1. IOError
        2. ImportError
        3. ValueError
        4. Division by zero
        5. KeyboardInterupted
        6. EOFError
        '''
print(f"Hasil pembagian adalah {hasil}")