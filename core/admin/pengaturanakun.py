# Logic Pengaturan Akun

from core.admin.account.hapusakun import hapusAkun
from core.admin.account.tambahakun import tambahAkun
from core.admin.account.ubahpassword import ubahPassword


def pengaturanAkun():
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
        tambahAkun()
    elif pilihAkun == 2:
        ubahPassword()
    elif pilihAkun == 3:
        hapusAkun()

    return pengaturanAkun()