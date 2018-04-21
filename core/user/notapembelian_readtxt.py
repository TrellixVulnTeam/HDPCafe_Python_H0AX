# Manggil File Txt

import json
import os

def notapembelian():
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'user.txt')
    conn=open(filename, "r")
    acc=json.load(conn)
    conn.close()
    return notapembelian()