# Membuat Login Yuhuuu, Ahaydeee!

def auth():
    usernameAdmin = input("Masukan Username = ")
    passwordAdmin = input("Masukan Password = ")
    if (usernameAdmin == 'admin' and passwordAdmin == 'admin'):
        print("Selamat Datang ponchoe ganteng! :D")
    else:
        print("Username atau Password Salah!")

    return auth()