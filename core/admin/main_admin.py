# Tampilan Awal Admin

import os.path

from core.admin.updatebarang import updateBarang
from core.admin.hapusbarang import hapusBarang
from core.admin.caribarang import cariBarang
from core.admin.lihatbarang import lihatBarang
from core.admin.pengaturanakun import pengaturanAkun
from core.admin.simpanData import simpanData
from core.admin.tambahbarang import tambahBarang


def main_admin():
    loop = True
    while loop:
        print()
        #print("Selamat Datang Di HDP Mart")
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

        if os.path.exists("barang.txt"):
            L=lihatBarang()
            if pilih == 1:
                L1=tambahBarang(L)
                simpanData(L1)
            elif pilih == 2:
                L1=updateBarang(L)
                simpanData(L1)
            elif pilih == 3:
                pass
                #hapusbarang()
            elif pilih == 4:
                pass
                #caribarang()
            elif pilih == 5:
                for x in L:
                    print(x)
                input()
            elif pilih == 6:
                pass
                #pengaturanakun()
            elif pilih == 7:
                break
            else:
                print("Menu tidak ditemukan")
                input()
        else:
            L=[]
            if pilih == 1:
                L1=tambahBarang(L)
                simpanData(L1)
            elif pilih == 7:
                break
            elif pilih == 2 or pilih == 3 or pilih == 4 or pilih == 5 or pilih == 6:
                print("File 'barang' belum ada, buat terlebih dahulu")
                input()
            else:
                print("Menu tidak ditemukan")
                input()
    return pilih
