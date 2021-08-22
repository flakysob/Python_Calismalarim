a = input("Bir sayı girin : ")

while True:
    if(a=="q"):
        print("Çıkış yapılıyor.")
        break
    else:
        a = int(a)
        liste = []

        for i in range(2,a+1):
            if(a%i==0):
                liste.append(i)
        print("Tam bölenleri = ", liste)
    break
        
