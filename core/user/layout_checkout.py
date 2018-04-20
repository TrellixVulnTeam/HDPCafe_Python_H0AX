# logic untuk layout checkout

def checkout():
    print()
    print("========================")
    print("HDP's Cafe CHECKOUT")
    print("========================")
    print()
    print("Berikut adalah Total Pembayaran dari Pembelanjaan anda :")
    print()
    print("Mie Goreng Telor Setengah Mateng Pedas - Rp 12000")
    print("Bengbeng - Rp 1500")
    print("Capcay Pedas Mampus - Rp 12000")
    print("Susu Ultra 1 liter - Rp 8000")
    print("Kopi Vietnam - Rp 18000")
    print()
    print("==========================")
    print("Total Harga : Rp 51.500")
    print()
    print("Lanjutkan Pembayaran?")
    print()
    print("1. Ya")
    print("2 . Batalkan")
    print()
    pilihCheckout = int(input("Masukan Pilihan = "))

    if pilihCheckout == 1 :
        lanjutPembayaran()
    elif pilihCheckout ==2 :
        print("Pesanan Anda dibatalkan, Tekan Enter untuk Kembali ke Menu.")
    else:
        print("Menu tidak ditemukan")
        input()
    return pilihCheckout

def lanjutPembayaran():
    print()
    print("==========================")
    print("Lanjut Pembayaran")
    print("==========================")
    print()
    print("Total Harga : Rp 51.500")
    print()
    uangKonsumen = input("Silahkan Input Uang Anda, Untuk Membayar")
    if (uangKonsumen > 51500) :
        print("Pembayaran Berhasil, Uang Kembalian Anda Rp 0")
        print()
        nota = input("Apakah anda ingin mencetak receipt? (Y/N) : ")
        if (nota == "Y", "y") :
            print("Mencetak nota..")
        else :
            print("Tidak Mencetak nota, Silahkan Tekan Enter untuk Kembali.")
    else :
        print("Uang Tidak Mencukupi")


    return lanjutPembayaran()