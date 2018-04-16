# Logic Tambah Barang kedalam list "L"

def tambahBarang(L):
    print("Masukkan Kode Barang\t\t: ", end="")
    id = int(input())
    print("Masukkan Nama Barang\t\t: ", end="")
    nama = input()
    print("Masukkan nilai Harga Barang\t: ", end="")
    harga = int(input())

    record=[id,nama,harga]
    L.append(record)
    return L