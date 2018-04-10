# Membuat Authentikasi

# untuk ini buat jalaninnya harus pake CMD gabisa pake pycharm, soalnya di pycharm masih ada bugnya masalah getPass!

import getpass

def auth():
    usernameAdmin = input("Masukan Username = ")
    passwordAdmin = getpass.getpass("Masukan Password")

    if (usernameAdmin == 'admin' and passwordAdmin == 'admin'):
        print("Selamat Datang!")
    else:
        print()
        print("Username atau Password Salah!")
        print()

    return auth()