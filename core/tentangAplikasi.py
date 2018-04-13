# Digunakan untuk menampilan Tentang Aplikasi

def tentangAplikasi():
    print()
    print("Aplikasi ini dibuat oleh..")
    print("")
    print("Hilman Abdan - 123123")
    print("Mega Ardila - 123123")
    print("Arief Wardhana - 1302173122")
    print("")
    print("Pembimbing : RZP")
    print()
    print("Ilmu Komputasi, Tugas Besar Algoritma Dasar Pemograman 2018.")

    print()
    print("====================================")
    print("Kembali Ke Menu Sebelumnya?")
    print("====================================")
    print()
    print("1. Ya")
    print("2. Tidak")
    print()
    pilihKembali = int(input("Masukkan Pilihan : "))

    if pilihKembali == 1:
        print("Kembali")
    elif pilihKembali == 2:
        print("Tidak Jadi")

    return tentangAplikasi()