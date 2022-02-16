# latihan komparasi dan logika

# membuat gabungan area rentang dari angka

'''

### GABUNGAN (OR)
### +++++++3-----------10++++++++

inputUser = float(input('Masukkan angka yang bernilai\nkurang dari 3\natau\nlebih besar dari 10\n: '))

# ++++++++3-----------------
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print('Kurang dari 3 =',isKurangDari)

# -------------------10++++++++++
# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print('Lebih dari 10 =',isLebihDari)

isCorrect = isKurangDari or isLebihDari
print('Angka yang anda masukkan kurang dari 3 atau lebih dari 10 adalah =',isCorrect)

'''


### IRISAN (DAN)
### --------3++++++++++10----------

print('\n',10*'=','\n')

inputUser = float(input('Masukkan angka yang bernilai\nlebih dari 3\ndan\nkurang dari 10\n: '))

# -------------3++++++++++++
# memeriksa angka lebih dari 3
isLebihDari = (inputUser > 3)
print('Lebih dari 3 =',isLebihDari)

# ++++++++++++++10-------------------
# memeriksa angka kurang dari 10
isKurangDari = (inputUser < 10)
print('Kurang dari 10 =',iskurangDari)

isCorrect = isKurangDari and isLebihDari
print('Angka yang anda masukkan lebih dari 3 dan kurang dari 10 adalah =',isCorrect)