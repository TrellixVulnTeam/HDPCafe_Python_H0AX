# logic untuk layout checkout

def checkout(La, total):
    print()
    print("========================")
    print("HDP's Cafe CHECKOUT")
    print("========================")
    print()
    print("Berikut adalah Total Pembayaran dari Pembelanjaan anda :")
    print()
    for x in La:
        print(str(x[1])+"---"+"Rp."+str(x[2]))
    print()
    print("==========================")
    print("Total Harga :", "Rp."+str(total))
    input()
    print("Lanjutkan Pembayaran?")
    print()
    print("1. Ya")
    print("2. Batalkan")
    print()
    loop = True
    while loop:
        try:
            pilihCheckout = int(input("Masukan Pilihan = "))
        except ValueError:
            pilihCheckout = 0
        if pilihCheckout == 1 :
            lanjutPembayaran(La, total)
            La = []
            total = 0
            break
        elif pilihCheckout ==2 :
            print("Pesanan Anda dibatalkan, Tekan Enter untuk Kembali ke Menu.")
            La=[]
            total=0
            break
        else:
            print("Menu tidak ditemukan")
            input()
    return La, total

def lanjutPembayaran(La, total):
    print()
    print("==========================")
    print("Lanjut Pembayaran")
    print("==========================")
    print()
    print("Total Harga :", "Rp."+str(total))
    print()
    uangKonsumen = int(input("Silahkan Input Uang Anda, Untuk Membayar : "))
    if (uangKonsumen > total):
        kembali = uangKonsumen-total
        print("Kembalian anda :", "Rp."+str(kembali))
        nota = input("Apakah anda ingin mencetak receipt? (Y/N) : ")
        if nota == "Y" or nota == "y" :
            print("Mencetak nota..")
        elif nota == "N" or nota == "n":
            print("Tidak Mencetak nota, Silahkan Tekan Enter untuk Kembali.")
    else :
        print("Uang Tidak Mencukupi")
