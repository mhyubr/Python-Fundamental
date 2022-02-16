# list sebagai iterable
makanan = ['coto','jalangkote','pallubasa','sop saudara','onde onde']

# for g in makanan:
#     print(g)
#     print(len(g))

# # string sebagai iterable

# bakwan = 'bakwan'

# for i in bakwan:
#     print(i)

# for di dalam for

buah = ['semangka','jeruk','apel','anggur']
sayur = ['kangkung','wortel','tomat','kentang']

daftar_belanja = [makanan,buah,sayur]

# print(daftar_belanja)

for subDaftarBelanja in daftar_belanja:
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:
        print(komponen)

for i in reversed(range(1, 10, 1)) :
    print(i)