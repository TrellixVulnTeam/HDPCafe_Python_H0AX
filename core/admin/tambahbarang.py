# Logic Tambah Barang kedalam list "L"

def tambahBarang(L):
    loop = True
    while loop:
        x = len(L)
        print("Masukkan nama barang", end=": ")
        nama = input()
        print("Masukkan harga barang", end=": ")
        harga = int(input())
        L1=[x+1,nama,harga]
        L.append(L1)
        for a in L:
            print(a)
        loop2 = True
        while loop2:
            print("Apakah anda ingin menambahkan barang lagi?(Y/N)", end=": ")
            jawab=input()
            if jawab == "N" or jawab == "n":
                loop=False
                break
            elif jawab == "Y" or jawab == "y":
                break
            else:
                print("Input salah")
                input()
    return L