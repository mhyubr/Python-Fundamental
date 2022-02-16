'''
Hal yang dibutuhkan dalam menginstal Eksternal Package, yaitu:
1. Python sudah terinstal
2. Koneksi Internet (karena didownload via internet)
3. Dependency

Package diinstal dengan menggunakan pip (pip untuk windows / pip3 untuk mac)
1. Buka terminal
2. ketik 'python --version' atau 'python3 --version' (untuk melihat versi python)
3. ketik 'pip --version' atau 'pip3 --version' (untuk melihat versi pip)
4. ketik 'pip list --format=colums' atau 'pip3 list --format=colums'  (untuk melihat package pip)
5. ketik 'python -m pip install –upgrade pip' (untuk mengupgrade pip)

Contoh Package eksternal yaitu Numpy, Matplotlib, Pandas, Pillow, opencv, dll
Adajuga Framework seperti Django, Flask, Pyramid, dll
Cara menginstall Numpy
1. Buka terminal 
2. ketik 'pip install numpy' atau 'pip3 install numpy'
3. atau dengan menggunakan 'python -m pip install numpy'
4. ketik 'pip uninstall numpy' atau 'pip3 uninstall numpy' (untuk uninstal numpy)
'''
import numpy as np
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
print(a+b)