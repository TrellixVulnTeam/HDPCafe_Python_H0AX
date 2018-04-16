# logic untuk tambah akun

def tambahAkun(L):
    print()
    print("===========================")
    print("Tambah Akun HDP Mart.")
    print("===========================")
    print()
    print("Masukkan Username\t\t: ", end="")
    id = input()
    print("Masukkan Password\t\t: ", end="")
    password = input()

    recordAkun=[id,password]
    L.append(recordAkun)
    return L