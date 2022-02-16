# latihan koncersi satuan temperature

# program konversi termperatur

print("\n========== PROGRAM KONVERSI TEMPERATUR ==========\n")
celcius = float(input('Masukkan suhu dalam celcius : '))

# Celcius
print("suhu dalam celcius adalah", celcius, "celcius")

# Reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah", reamur, "reamur")

# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah", fahrenheit, "fahrenheit")

# Kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah", kelvin, "kelvin")