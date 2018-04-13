# Tampilan Awal Admin

from core.tentangAplikasi import tentangAplikasi
from core.keluarAplikasi import keluarAplikasi
from core.auth import auth

#Pendukung untuk membuat Asci Art
import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

#Asci Art, terlalu banyak font ASCI dan gw masih binggung font yang bagus apa..
init(strip=not sys.stdout.isatty())
cprint(figlet_format('HDP MART!', font='isometric4'))


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
    pilih = int(input("Masukkan Pilihan : "))

    if pilih == 1:
        auth()
    elif pilih == 2:
        nama = input("Masuk Pembeli")
    elif pilih == 3:
        print(tentangAplikasi())
    elif pilih == 4:
        keluarAplikasi()

    return main_admin()