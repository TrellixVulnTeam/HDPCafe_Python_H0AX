# Tampilan Awal Aplikasi HDP Mart

from core.tentangAplikasi import tentangAplikasi
from core.keluarAplikasi import keluarAplikasi
from core.auth import auth
from core.user import main_user

#Pendukung untuk membuat Asci Art
import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

#Asci Art, terlalu banyak font ASCI dan gw masih binggung font yang bagus apa..
init(strip=not sys.stdout.isatty())
cprint(figlet_format('HDP MART!', font='isometric4'))


#Menu Utama
print("Selamat Datang di HDP Mart!")
print()
print("=============")
print("1. Masuk Sebagai Admin")
print("2. Masuk Sebagai Pembeli")
print("3. Tentang Aplikasi")
print("4. Keluar")
print("=============")
print()
pilih=int(input("Masukkan Pilihan : "))


if pilih == 1 :
    auth()
elif pilih==2 :
    main_user()
elif pilih==3 :
    print(tentangAplikasi())
elif pilih==4 :
    keluarAplikasi()