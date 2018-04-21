# Native Nota Menggunakan ASCII

#Pendukung untuk membuat Asci Art
import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

#Asci Art, terlalu banyak font ASCI dan gw masih binggung font yang bagus apa..
init(strip=not sys.stdout.isatty())
cprint(figlet_format('HDP Cafe!', font='starwars'))

def notanative():
    print()
    print("--------------------------------------------------")
    print("                     Nota Pembelian")
    print("                        HDP CAFE")
    print("                  Jalan Cafetaria No 6")
    print("--------------------------------------------------")
    print()
    print("Daftar Barang yang telah anda beli : ")
    print()
    print("1. Indomie Dobel Telor - Rp 12000")
    print("2. AQUA Botol - Rp 3000")
    print()
    print("Total Belanja : Rp 15000")
    print()
    print("Uang yang diberikan : Rp 20000")
    print("Kembalian : Rp 5000")
    print()
    print("Terimakasih Sudah Datang Ke HDP Cafe!")
    print()
    print("--------------------------------------------------")

    return notanative()