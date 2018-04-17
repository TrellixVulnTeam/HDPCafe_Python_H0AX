# logic untuk tambah akun

def tambahAkun(L):
    print()
    print("===========================")
    print("Tambah Akun HDP's Cafe.")
    print("===========================")
    print()
    print("Masukkan Username\t\t: ", end="")
    user = input()
    print("Masukkan Password\t\t: ", end="")
    password = input()
    La=[user, password]
    L.append(La)
    return L