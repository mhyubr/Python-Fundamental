# operator bitwise || operasi biner || binary

a = 9
b = 5

# bitwise OR (|)
c = a | b
print('\n',10*'=','OR',10*'=')
print('nilai :',a,', binary',format(a,'08b'))
print('nilai :',b,', binary',format(b,'08b'))
print(30*'=','(|)')
print('nilai :',c,', binary',format(c,'08b'))

# bitwise AND (&)
c = a & b
print('\n',10*'=','AND',10*'=')
print('nilai :',a,', binary',format(a,'08b'))
print('nilai :',b,', binary',format(b,'08b'))
print(30*'=','(&)')
print('nilai :',c,', binary',format(c,'08b'))

# bitwise XOR (^)
c = a ^ b
print('\n',10*'=','XOR',10*'=')
print('nilai :',a,', binary',format(a,'08b'))
print('nilai :',b,', binary',format(b,'08b'))
print(30*'=','(^)')
print('nilai :',c,', binary',format(c,'08b'))

# bitwise NOT (~)
c = ~a
print('\n',10*'=','NOT',10*'=')
print('nilai :',a,', binary',format(a,'08b'))
print(30*'=','(~)')
print('nilai :',c,', binary',format(c,'08b'))
print(30*'=','(^)')
d = 0b0000001001
e = 0b1111111111
print('nilai :',e^d, ', binary',format(c,'08b'))

## shifting

# shift right (>>)
c = a >> 2
print('\n',10*'=',' >> ',10*'=')
print('nilai :',a,', binary',format(a,'08b'))
print(30*'=','(>>)')
print('nilai :',c,', binary',format(c,'08b'))

# shift left (<<)
c = a << 2
print('\n',10*'=',' << ',10*'=')
print('nilai :',a,', binary',format(a,'08b'))
print(30*'=','(<<)')
print('nilai :',c,', binary',format(c,'08b'))