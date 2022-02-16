Data = [1,4,9,16,25,36,49,64,"hello",True,False,12.5,20,5]

# mengakses list
Subdata1 = Data[0]
Subdata2 = Data[-3]

# memotong list
Subdata3 = Data[2:7]
Subdata4 = Data[:4]

# menambah list
Data2 = [100,200,300,400,500,600,700,800,900]
Data3 = Data + Data2

# merubah content dari list
# print(Data)
Data[4] = 87
# print(Data)

## mengcopy list ke variabl baru
a = Data[:]
# harus menggunakan [:] agar Data tidak bisa diubah oleh variabel a
a[4] = 13
#print(a)
#print(Data)

# merubah content list dengan degan menggunakan metode slicing
Data[3:5] = [11,12]
# print(Data)

# List dalam list
x = [Data,Data2]
# print(x)

# mengakses list dalam multidimensional list
y = x[0][3]
# print(y)

# methods untuk list
Data.append(Data2) # menambah member list
#print(Data)

# function yang bisa kita gunakan kepada list
panjang_list = len(Data) # menghitung panjang list
print(panjang_list)


# print(Subdata1)
# print(Subdata2)
# print(Subdata3)
# print(Subdata4)
# print(Data3)