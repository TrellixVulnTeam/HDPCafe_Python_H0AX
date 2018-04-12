# Membuat Authentikasi

# untuk ini buat jalaninnya harus pake CMD gabisa pake pycharm, soalnya di pycharm masih ada bugnya masalah getPass!

import getpass
import os
import header

def auth():
    print("=============================")
    print("Selamat Datang di HDP Mart!")
    print("=============================")
    print()

    z = 'ya'
    a = 0
    while z == 'ya' :
        user = input('Username = ')
        pwd = getpass.getpass('Password = ')
        if (user =='admin') and (pwd =='admin') :
            print ('Selamat Datang',user,'Tekan Enter untuk lanjut')
            input()
            break
        elif (user =='admin') or (pwd =='mimin') :
            print ('Username/Password salah')
        else :
            print('Password Salah')
        a = a+1
        if a == 3 :
            print ('sudah 3x input')
            break
        print()
        z = input('Input username dan password lagi ? ya/tidak ?')
        print()
        os.system('cls')
        header.header()