print("******************* \n Kullanıcı Girişi \n *******************")
girisHakki = 2
userName = "tahdgn"
password = "12345"

while True:
    kullaniciadi=input("Kullanıcı adı : ")
    sifre = input("Şifre : ")

    if(kullaniciadi != userName and sifre != password):
        print("Hatalı giriş. Kalan deneme hakkı = ", girisHakki)
        girisHakki -= 1
        if(girisHakki < 0):
            print("Hesabınız bloke olmuştur.")
            break
    else:
        print("Sisteme başarı ile giriş yapıldı.")