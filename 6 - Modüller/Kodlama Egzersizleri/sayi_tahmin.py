import sayi_tahmini_modul
a = input("Tahminin : ")
tahminhakki = 3

if(a == "q"):
    print("Çıkış yapılıyor.")
else: 
    a = int(a)
    x = sayi_tahmini_modul.Tahmin(a)
    while (tahminhakki > 1):
        if(x == True):
            print("Tebrikler. Tahmin doğru!")
            break
        else:
            tahminhakki = tahminhakki - 1
            print("Tekrar deneyin. Kalan tahmin hakkı = ", tahminhakki)
            a = input("Tahminin : ")