
def asalsayibulucu(sayi):
    if(sayi == 1):
        return False
    elif(sayi == 2):
        return True
    else:
        for i in range(2,sayi):
            if(sayi%i==0):
                return False
        return True


while True:
    a = input("Bir sayı girin (Çıkmak için q tuşuna basın) : ")
    if(a =="q"):
        break
    else:
        a = int(a)

        if(asalsayibulucu(a)):
            print(a,"asal bir sayıdır")
        else:
            print(a,"asal bir sayı değildir.")





