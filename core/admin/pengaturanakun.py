# Logic Pengaturan Akun

from core.admin.account.hapusakun import hapusAkun
from core.admin.account.tambahakun import tambahAkun
from core.admin.account.ubahpassword import ubahPassword
from core.admin.simpanData import simpanData
from core.admin.lihatmenu import lihatMenu
import os.path



def pengaturanAkun(user):
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'user.txt')
    L = lihatMenu(filename)
    loop=True
    while loop:
        print()
        print("=======================")
        print("Pengaturan Akun")
        print("=======================")
        print()
        print("1. Tambah Akun")
        print("2. Ubah Password")
        print("3. Hapus Akun")
        print("4. Kembali")
        print()
        pilihAkun = int(input("Masukkan Pilihan : "))

        if pilihAkun == 1:
            La=tambahAkun(L)
            if not La:
                pass
                print("Pass")
            else:
                simpanData(La, filename)
        elif pilihAkun == 2:
            La=ubahPassword(L, user)
            simpanData(La, filename)
        elif pilihAkun == 3:
            La=hapusAkun(L)
            simpanData(La, filename)
        elif pilihAkun == 4:
            break
        else:
            print("Input salah")
            input()