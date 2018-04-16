# menampilkan data dari parameter b

def lihatData(b):
    print("Kode Barang\tNama Barang\tHarga Barang")

    for x in range(len(b)):
        print('%s\t%s\t%s' % (b[x][0], b[x][1], b[x][2]))
