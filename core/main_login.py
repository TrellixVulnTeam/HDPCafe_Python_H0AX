# Tampilan Awal Aplikasi HDP Mart

from core.tentangAplikasi import tentangAplikasi
from core.keluarAplikasi import keluarAplikasi
from core.auth import auth

print("=============")
print("1. Masuk Sebagai Admin")
print("2. Masuk Sebagai Pembeli")
print("3. Tentang Aplikasi")
print("4. Keluar")
print("=============")
pilih=int(input("Masukkan Pilihan : "))


if pilih == 1 :
    auth()
elif pilih==2 :
    nama = input("Masuk Pembeli")
elif pilih==3 :
    print(tentangAplikasi())
elif pilih==4 :
    keluarAplikasi()