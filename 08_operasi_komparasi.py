# operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean

# > , < , >= , <= , == , != , is , is not

a = 4
b = 2

print("\n============== LEBIH BESAR DARI (>) ==============")
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

print("\n============== KURANG DARI (<) ==============")
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

print("\n============== LEBIH BESAR DARI SAMA DENGAN (>=) ==============")
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

print("\n============== KURANG DARI SAMA DENGAN (<=) ==============")
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

print("\n============== SAMA DENGAN (==) ==============")
hasil = a == 3
print(a,'==',3,'=',hasil)
hasil = b == 3
print(b,'==',3,'=',hasil)
hasil = b == 2
print(b,'==',2,'=',hasil)

print("\n============== TIDAK SAMA DENGAN (!=) ==============")
hasil = a != 3
print(a,'!=',3,'=',hasil)
hasil = b != 3
print(b,'!=',3,'=',hasil)
hasil = b != 2
print(b,'!=',2,'=',hasil)



x = 5 # ini adalah assignment membuat object
y = 5

# 'is' sebagai komparasi object identity
print("\n============== OBJECT IDENTITY (is) ==============")

print('nilai x =',x,'id =', hex(id(x)))
print('nilai x =',y,'id =', hex(id(y)))
# jika terdapat nilai yang sama maka akan dimasukkan di memori (hex) yang sama
hasil = x is y
# tidak boleh dibandingkan dengan literal atau nilainya (x is 5)
print('x is y =',hasil)


print("\n============== OBJECT IDENTITY (is not) ==============")

print('nilai x =',x,'id =', hex(id(x)))
print('nilai x =',y,'id =', hex(id(y)))
# jika terdapat nilai yang sama maka akan dimasukkan di memori (hex) yang sama
hasil = x is not y
# tidak boleh dibandingkan dengan literal atau nilainya (x is not 5)
print('x is not y =',hasil)