print("******************************\n ATM \n ******************************")
bakiye = 1000

while True:
    secim = int(input(
        " 1-Bakiye sorgulama \n 2-Para Yatırma \n 3-Para Çekme \n 4-Çıkış \n Yapmak istediğiniz işlemi seçin\n"))
    if(secim == 1):
        print("Bakiye {} TL.".format(bakiye))
        continue
    elif(secim == 2):
        yatir = int(input("Yatırılacak miktarı girin : "))
        bakiye = bakiye + yatir
        print("Bakiye {} TL".format(bakiye))

    elif(secim == 3):
        cek = int(input("Çekeceğiniz miktarı girin : "))
        if(bakiye-cek < 0):
            print("Yetersiz bakiye. Lütfen geçerli bir tutar girin. Çekebileceğiniz en yüksek miktar {} TL".format(bakiye))
            continue
        bakiye = bakiye - cek
        print("Paranız veriliyor. Kalan bakiye {} TL ".format(bakiye))
    elif(secim == 4):
        print("Yine bekleriz")
        break
    else:
        print("Geçersiz işlem")