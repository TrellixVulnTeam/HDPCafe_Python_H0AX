# Logic hapus barang, untuk menghapus elemen terakhir dari list L

def hapusBarang(L):
    n = len(L)
    for x in L:
        print(x)
    loop = True
    while loop:
        i=0
        print("Pilih id barang yang ingin dihapus", end=": ")
        id = int(input())
        while i <= (n - 1) and L[i][0] != id:
            i = i + 1
        if L[i][0] == id:
            hapus=L.pop(i)
            for x in L:
                print(x)
        else:
            print("Barang dengan id", id, "tidak ditemukan")
            input()
        loop2 = True
        while loop2:
            print("Apakah anda ingin menghapus barang dengan id lain?(Y/N)", end=": ")
            jawab = input()
            if jawab == "Y" or jawab == "y":
                break
            elif jawab == "N" or jawab == "n":
                loop = False
                break
            else:
                print("Input salah")
                input()
    return L
