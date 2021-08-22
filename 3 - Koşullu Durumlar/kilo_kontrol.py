b = float(input("boyunuzu metre cinsinden girin"))
k = float(input("kilonuzu kg cinsinden girin(örneğin 74.6)"))
bki = k / (b*b)
if(bki < 18.5):
    print(bki)
    print("Zayıf")
elif(18.5<bki<25):
    print(bki)
    print("Normal")
elif(25<bki<30):
    print(bki)
    print("Fazla kilolu")
elif(30<bki):
    print(bki)
    print("Obez")
else:
    print("Hatalı giriş.")