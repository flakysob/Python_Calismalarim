

def tambolen(sayi):
    tam_bolenler = []

    for i in range(2,sayi):
        if(sayi % i == 0):
            tam_bolenler.append(i)
    return tam_bolenler

while True:
    sayi = input("sayi : ")
    if(sayi=="q"):
        print("Program sonlandırılıyor.")
        break
    else:
        sayi = int(sayi)
        print("Girilen sayının tam bölenleri", tambolen(sayi))
