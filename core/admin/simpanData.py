# Menyimpan data bersadarkan parameter 'L' sebagai list dan 'nama' sebagai nama file

import json
def simpanData(L):
    with open('barang.txt', 'w') as file:
        json.dump(L, file)
        print("Data barang berhasil disimpan, tekan enter untuk melanjutkan")
        input()