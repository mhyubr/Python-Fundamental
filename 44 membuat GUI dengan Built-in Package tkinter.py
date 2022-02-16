'''
Package Built-in yaitu Package yang sudah terinstall bersama dengan penginstalan python
contohnya : math, os, tkinter, dll
'''
import tkinter

main_window = tkinter.Tk()

def event_tekan():
    label2 = tkinter.Label(main_window, text="aku ditekan ^_^")
    label2.pack() # menyimpal label2

label = tkinter.Label(main_window, text="halo, saya adalah \n GUI sederhana dengan \n menggunakan python")
tombol = tkinter.Button(main_window, text="Tekan Aku", command = event_tekan) # command = event_tekan untuk menghubung ke def event_tekan()
label.pack() # menyimpan label
tombol.pack() # menyimpan tombol
main_window.mainloop() # akan menunggu di close (muncul terus sampali di close)