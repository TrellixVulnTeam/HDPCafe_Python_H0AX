# Menyimpan data bersadarkan parameter 'L' sebagai list dan 'nama' sebagai nama file

import json

def simpanData(L, nama):
    with open(nama + '.txt', 'w') as file:
        json.dump(L, file)
