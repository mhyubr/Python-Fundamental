# operasi assignment yaitu operasi yang daat dilakukan dengan penyingkatan
# artinya operasi ditambah dengan assignment


## operasi aritmatika
a = 5 # adalah assignment
print("nilai a :", a)

a += 1 # artinya adalah a = a + 1
print("nilai a += 1, nilai 'a' menjadi :", a)

a -= 2 # artinya adalah a = a - 2
print("nilai a -= 2, nilai 'a' menjadi :", a)

a *= 5 # artinya adalah a = a * 5
print("nilai a *= 5, nilai 'a' menjadi :", a)

a /= 2 # artinya adalah a = a / 2
print("nilai a /= 2, nilai 'a' menjadi :", a)



## modulus dan floor division

b = 10
print("\nnilai b =", b)

b %= 3
print("nilai a %= 3, nilai 'b' menjadi :", b)


c = 10
print("\nnilai c =", c)

c //= 3
print("nilai c //= 3, nilai 'c' menjadi :", c)

d = 5
print("\nnilai d =", d)


# pangkat atau eksponen

d **= 3
print("nilai d **= 3, nilai 'd' menjadi :", d)


## operasi bitwise

# OR
f = True
print("\nnilai f =", f)
f |= False
print("nilai f |= False, nilai 'f' menjadi :", f)
f = False
print("\nnilai f =", f)
f |= False
print("nilai f |= False, nilai 'f' menjadi :", f)

# AND
f = True
print("\nnilai f =", f)
f &= False
print("nilai f &= False, nilai 'f' menjadi :", f)
f = True
print("\nnilai f =", f)
f &= True
print("nilai f &= True, nilai 'f' menjadi :", f)

# XOR
f = True
print("\nnilai f =", f)
f ^= False
print("nilai f ^= False, nilai 'f' menjadi :", f)
f = True
print("\nnilai f =", f)
f ^= True
print("nilai f ^= True, nilai 'f' menjadi :", f)

# geser geser
d = 0b0100
print("\nnilai d =", format(d, '04b'))
d >>= 2
print("nilai d >>= 2, nilai 'd' menjadi", format(d, '04b'))
d <<= 1
print("nilai d <<= 1, nilai 'd' menjadi", format(d, '04b'))