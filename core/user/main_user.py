# Tampilan Awal User

from core.auth import auth
import os

def main_user():
    print("Selamat Datang Di HDP Mart")
    print()
    print("=============")
    print("1. Menu User 1")
    print("2. Menu User 1")
    print("3. Menu User 1")
    print("4. Menu User 1")
    print("=============")
    print()
    pilih = int(input("Masukan Pilihan = "))

    if pilih == 1 :
        print("hi 1")
    elif pilih ==2 :
        print("hi 2")
    elif pilih == 3 :
        print("hi 3")
    elif pilih == 4 :
        print("hi 4")
    return pilih