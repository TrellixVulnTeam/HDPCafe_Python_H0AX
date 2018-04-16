# Logic untuk pilihan melihat barang
import json
def lihatBarang():
    op=open("barang.txt", "r")
    L=json.load(op)
    op.close()
    L.sort()
    return L