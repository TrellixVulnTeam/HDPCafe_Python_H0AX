# Logic untuk Hapus Akun

def hapusAkun():
    print()
    print("==============================================")
    print("PERINGATAN!!")
    print()
    print("Apakah Anda yakin untuk menghapus akun ini?")
    print("==============================================")
    print()
    print("1. Ya")
    print("2. Tidak")
    print()
    pilihHapus = int(input("Masukkan Pilihan : "))

    if pilihHapus == 1:
        print("Akun Dihapus!")
    elif pilihHapus == 2:
        print("Tidak Jadi :D")