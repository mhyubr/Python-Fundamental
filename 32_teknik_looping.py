# teknik looping

# LIST
nama_band = [
    'Payung Teduh',
    'Foutwnty',
    'Dialog Dini Hari',
    'Mr. Sonjaya',
    'Parahyena'
]

daftar_lagu = [
    'akad',
    'Zona Nyaman',
    'Sang Filsuf',
    'Sindoro'
]

# enumerate
for i, band in enumerate(nama_band) :
    print(i,':', band)

# zip
for band, lagu in zip(nama_band, daftar_lagu) :
    print(band,"-",lagu)


# SET
playlist = {'baby baby', 'ada apa dengan cinta', 'cenat cenut', 'ketika cinta bertasbih'}

# urutan akan acak karena menggunakan set
for lagu in playlist :
    print(lagu)

# urut berdasarkan abjad
for lagu in sorted(playlist) :
    print(lagu)


# DICTIONARY
playlist2 = {
    'Payung Teduh':'akad',
    'Fouttwnty':'Zona Nyaman',
    'Dialog Dini Hari':'Rumahku'
}

for i in playlist2.keys():
    print(i)

for i in playlist2.values():
    print(i)

for i, v in playlist2.items():
    print(i,"-",v)