# operasi logika atau boolean

# not , or , and , xor

# NOT
print('\n====== NOT ======')
a = True
c = not a
print("data 'a' =",a)
print('--------- NOT')
print("data 'c' =",c)

# OR
print('\n====== OR ======')
a = True
b = True
c = a or b
print(a,'OR',b,'  =',c)
a = True
b = False
c = a or b
print(a,'OR',b,' =',c)
a = False
b = True
c = a or b
print(a,'OR',b,' =',c)
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)

# AND
print('\n====== AND ======')
a = True
b = True
c = a and b
print(a,'AND',b,'  =',c)
a = True
b = False
c = a and b
print(a,'AND',b,' =',c)
a = False
b = True
c = a and b
print(a,'AND',b,' =',c)
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)

# OR
print('\n====== OR ======')
a = True
b = True
c = a or b
print(a,'OR',b,'  =',c)
a = True
b = False
c = a or b
print(a,'OR',b,' =',c)
a = False
b = True
c = a or b
print(a,'OR',b,' =',c)
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)

# XOR (Operator Bitwise)
print('\n====== XOR ======')
a = True
b = True
c = a ^ b
print(a,'XOR',b,'  =',c)
a = True
b = False
c = a ^ b
print(a,'XOR',b,' =',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,' =',c)
a = False
b = False
c = a and b
print(a,'XOR',b,'=',c)

a = 10
b = 3
a = a ^ b
print(a)
b = b ^ a
print(b)
a = a ^ b
print(a)