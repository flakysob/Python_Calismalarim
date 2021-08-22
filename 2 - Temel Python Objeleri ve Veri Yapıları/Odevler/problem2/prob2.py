boy = float(input("Boyunuzu metre cinsinden girin ( örneğin 1.89)"))
kilo = float(input("Kilonuzu kg cinsinden girin ( örneğin 90)"))
ind = kilo/(boy*boy)
print("{} boyunda olan ve {} kg ağırlığındaki birinin beden kitle indeksi {} olur.".format(boy,kilo,ind))
#format olmadan, print ile yazdırma işleminde içerisindeki değişkenleri string veri tipinde istiyor