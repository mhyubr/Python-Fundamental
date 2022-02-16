# string adalah kumpulan karakter

data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string
'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'menggunakan single quote'
print(data)
print('"Halo, apa kabar?"')

data = "menggunakan double quote"
print(data)
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# backslah
print("C:\\user\\Ayyub")

# tab
print("muh\tayyub\t\t\tramli")

# backspace
print("Muh\bAyyub")

# newline
print("muh\nayyub") # LF -> line feed -> unix, macos, linux
print("muh\rayyub") # CR -> carriage return -> commodore, acorn, lisp
print("muh\r\nayyub") # CRLF -> line feed carriage return -> windows


# 3. String literal atau raw

# hati - hati
print('C:\new folder') # akan salah pathnya

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama    : Muhammad Ayyub Ramli
NIM     : 1202201296
""")

# multiline literal string dan raw
print(r"""
Nama        : Muhammad Ayyub Ramli
NIM\kelas   : 1202201296\SI-44-01
Website     : www.yub.com/newID
""")