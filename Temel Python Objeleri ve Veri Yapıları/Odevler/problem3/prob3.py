print("Benzinin litre ücreti : 7.12")
benzin = 7.12
kmdeyaktigi = float(input("Aracınız 100 km'de kaç lt benzin harcıyor?"))
kmdeyaktigi = kmdeyaktigi/100
kackmgittigi = float(input("Kaç km yol yaptınız/yapacaksınız?"))
x = kmdeyaktigi*kackmgittigi
y = benzin * x
print("{} tl ücret ödemeniz gereklidir.".format(y))