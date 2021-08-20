print("Çıkmak için q'ya basın ")
while True:
    sayi = input("Sayı : ")
    if(sayi=="q" or sayi=="Q"):
        print("Program sonlandırılıyor.")
        break
    else:
        sayi = int(sayi)
        faktoriyel = 1

        for i in range(2,sayi+1):
            faktoriyel *= i
        print("Girilen sayının faktöriyeli = ", faktoriyel)
