# Logic untuk ubah Password

def ubahPassword():
    print()
    print("==============================================")
    print("PERINGATAN!!")
    print()
    print("Anda akan merubah password anda, jika anda lupa")
    print("dengan password anda silahkan hubungi admin..")
    print("==============================================")
    print()
    print("1. Ubah Password")
    print("2. Kembali")
    print()
    pilihHapus = int(input("Masukkan Pilihan : "))

    if pilihHapus == 1:
        executePassword()
    elif pilihHapus == 2:
        print("Kembali ke Menu Pengaturan Akun")

    return ubahPassword()


def executePassword():
    print()
    print("==============================================")
    print("Silahkan Masukan Password lama anda!")
    print("==============================================")
    print()
    passLama = input("Password Lama = ")
    if (passLama == "admin"):
        print("Silahkan Masukan Password Baru!")
    else:
        print("Password Salah, Ulangi?")
        executePassword()

    return executePassword()


def passwordBaru():
    print()
    print("==============================================")
    print("Silahkan Masukan Password baru anda!")
    print("==============================================")
    print()
    passLama = input("Password Baru = ")
    if (passLama):
        print("Password Berhasil Diubah")
    else:
        print("Gagal Merubah Password, Ulangi?")
        passwordBaru()

    return passwordBaru()
