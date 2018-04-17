# Logic Pengaturan Akun

from core.admin.account.hapusakun import hapusAkun
from core.admin.account.tambahakun import tambahAkun
from core.admin.account.ubahpassword import ubahPassword
from core.admin.simpanData import simpanData
from core.admin.lihatbarang import lihatBarang
import os.path



def pengaturanAkun():
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'user.txt')
    L = lihatBarang(filename)
    print()
    print("==============================================")
    print("Pengaturan Akun")
    print("==============================================")
    print()
    print("1. Tambah Akun")
    print("2. Ubah Password")
    print("3. Hapus Akun")
    print()
    pilihAkun = int(input("Masukkan Pilihan : "))

    if pilihAkun == 1:
        La=tambahAkun(L)
        simpanData(La, filename)
    elif pilihAkun == 2:
        ubahPassword()
    elif pilihAkun == 3:
        hapusAkun()