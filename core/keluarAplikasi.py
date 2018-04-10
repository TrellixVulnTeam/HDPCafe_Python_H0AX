# Membuat Sebuah Fungsi untuk Keluar dari Aplikasi

def keluarAplikasi():
    print("Apakah Anda Yakin untuk Keluar dari Aplikasi?")
    print()
    print("=============")
    print("1. Ya")
    print("2. Tidak")
    print("=============")
    print()
    pilihKeluar = int(input("Masukkan Pilihan : "))

    if pilihKeluar == 1:
        exit()
    elif pilihKeluar == 2:
        print("Tidak Jadi Exit :D")

    return keluarAplikasi()