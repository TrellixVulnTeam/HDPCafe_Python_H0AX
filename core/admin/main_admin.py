# Tampilan Awal Admin

from core.admin import updatebarang
from core.admin import hapusbarang
from core.admin import caribarang
from core.admin import lihatbarang
from core.admin import pengaturanakun
from core.admin.tambahbarang import tambahBarang


def main_admin():
    print()
    print("Selamat Datang Di HDP Mart")
    print()
    print("==================================")
    print("1. Tambah Barang")
    print("2. Update Barang")
    print("3. Hapus Barang")
    print("4. Cari Barang")
    print("5. Lihat Barang")
    print("6. Pengaturan Akun")
    print("7. Kembali ke Menu Utama")
    print("==================================")
    print()
    pilih = int(input("Masukan Pilihan = "))

    if pilih == 1:
        tambahBarang()
    elif pilih == 2:
        updatebarang()
    elif pilih == 3:
        hapusbarang()
    elif pilih == 4:
        caribarang()
    elif pilih == 5:
        lihatbarang()
    elif pilih == 6:
        pengaturanakun()
    elif pilih == 7:
        print("yay Kembali")
    return pilih
