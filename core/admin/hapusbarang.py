# Logic hapus barang, untuk menghapus elemen terakhir dari list L

def hapusBarang(L):
    print("Apakah Anda yakin ingin menghapus barang ini?")
    print()
    print("1. Ya")
    print("2. Tidak")
    print()
    pilihHapus = int(input("Masukkan Pilihan : "))

    if pilihHapus == 1:
        L.pop
        print("Barang Dihapus")
    elif pilihHapus == 2:
        print("Tidak Jadi Dihapus :D")

    return hapusBarang,L
