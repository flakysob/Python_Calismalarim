print("///// Hesap makinesi uygulaması /////")

print("1 - toplama")
print("2 - çıkarma")
print("3 - çarpma")
print("4 - bölme")
islem = int(input("Hangi işlem yaplacak? \n"))
s1 = int(input("1. sayı : "))
s2 = int(input("2. sayı : "))

if(islem==1):
    son=s1+s2
    print("sonuç = ",son)
elif(islem==2):
    son = s1 - s2
    print("sonuç = ",son)
elif(islem==3):
    son = s1 * s2
    print("sonuç = ",son)
elif(islem==4):
    son = s1 / s2
    print("sonuç = ",son)
else:
    print("Hatalı giriş yaptınız.")