def asalmi(x):
    if(x==1):
        return False
    elif(x==2):
        return True
    else:
        for i in range(2,x):
            if(x%i==0):
                return False
            else:
                return True

while True:
    a = input("Sayı girin : ")

    if(a=="q"):
        print("Çıkış yapılıyor.")
        break
    else:
        a = int(a)
        if(asalmi(a)):
            print("Girilen değer asaldır.")
        else:
            print("Girilen değer asal değildir.")