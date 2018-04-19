# Tampilan Awal User

from core.user.layout_minuman import minuman
from core.user.layout_makanan import makanan
from core.user.layout_checkout import checkout

def main_user():
    print("Selamat Datang Di HDP Mart, Selamat Berbelanja!")
    print()
    print("==================================")
    print("1. Aneka Minuman")
    print("2. Aneka Makanan")
    print("3. Checkout")
    print("4. Kembali ke menu Utama")
    print("==================================")
    print()
    pilih = int(input("Masukan Pilihan = "))

    if pilih == 1 :
        minuman()
    elif pilih ==2 :
        makanan()
    elif pilih == 3 :
        checkout()
    elif pilih == 4 :
        print("Kembali ke menu Utama")
    else:
        print("Menu tidak ditemukan")
        input()
    return pilih