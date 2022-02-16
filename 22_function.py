# # mendefenisikan fungsi
# def fungsi():
#     print('ini adalah fungsi')

# # memanggil fungsi
# fungsi()
# fungsi()


# membuat fungsi sederhana

def suara_ayam():
    print("kukkuruyuk!!!")

def harga_ayam():
    print("harga ayam per 1 kg adalah Rp.20.000")

# membuat fungsu dengan input argumen

def harga_total_ayam(kg):
    suara_ayam()
    harga = 20.000
    harga_total = kg*harga
    print('harga',kg,'ayam adalah',harga_total)

harga_total_ayam(2)
harga_total_ayam(3)
harga_total_ayam(2.5)
harga_total_ayam(10)