import time
start_time = time.time()
print("hello world!")
print("World")

print("halo")
# ini adalah comment
a = 10 # ini juga comment
"""ini juga komen juga dong
"""
print(a)

print(time.time() - start_time, "detik")
# kita bisa mencompile python ke bytecode
# cara mengcompile, buka terminal dan jalankan perintah berikut
# python -m py_compile main.py  (main.py = nama file python)
# dan jalankan di folder __pycache__
