# Tampilan Awal Aplikasi HDP Mart

from core.tentangAplikasi import tentangAplikasi
from core.keluarAplikasi import keluarAplikasi
from core.admin.main_admin import main_admin
from core.user.main_user import main_user
from core.auth import auth

#Pendukung untuk membuat Asci Art
import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

#Asci Art, terlalu banyak font ASCI dan gw masih binggung font yang bagus apa..
init(strip=not sys.stdout.isatty())
cprint(figlet_format('HDP MART!', font='isometric4'))

loop=True
while loop:
    print("====================================")
    print("Selamat Datang Di HDP Mart")
    print("====================================")
    print()
    print("1. Masuk Sebagai Admin")
    print("2. Masuk Sebagai Pembeli")
    print("3. Tentang Aplikasi")
    print("4. Keluar")
    print()

    pilih=int(input("Masukkan Pilihan : "))
    if pilih == 1 :
        auth()
    elif pilih ==2 :
        main_user()
    elif pilih == 3 :
        tentangAplikasi()
    elif pilih == 4 :
        loop=False
        keluarAplikasi()
    else:
        print("Input salah")
        input()