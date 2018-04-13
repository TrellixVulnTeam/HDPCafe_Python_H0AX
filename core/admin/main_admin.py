# Tampilan Awal Admin

from core.auth import auth
import os

def main_admin():
    print("Selamat Datang Di HDP Mart")
    print()
    print("=============")
    print("1. Masuk Sebagai Admin")
    print("2. Masuk Sebagai Pembeli")
    print("3. Tentang Aplikasi")
    print("4. Keluar")
    print("=============")
    print()
    pilih = int(input("Masukan Pilihan = "))
    return pilih

os.system("cls")
pil = main_admin()
os.system("cls")
while pil != 4 :
    if pil == 1 :
        auth()
    elif (pil==2):
        print("Menu 2")
    elif (pil==3):
        print("Menu 3")
    elif (pil==4):
        print("Menu 4")
    os.system("cls")
    pil=main_admin()
    os.system("cls")