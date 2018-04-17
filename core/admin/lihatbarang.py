import json
def lihatBarang(nama):
    op=open(nama, "r")
    L=json.load(op)
    op.close()
    L.sort()
    return L