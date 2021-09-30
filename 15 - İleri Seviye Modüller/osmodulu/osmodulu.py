#Dosyalarda gezinme
import os


for klasoryolu,klasorisimleri,dosyaisim in os.walk("C:/Users/tahaslı/Desktop/Python/calisma/15 - İleri Seviye Modüller"):
    for i in dosyaisim:
        if(i.endswith(".py")):
            print(i)












"""
for klasoryolu,klasorisimleri,dosyaisim in os.walk("C:/Users/tahaslı/Desktop/Python/calisma/15 - İleri Seviye Modüller"):
    for i in dosyaisim:
        print(i)
"""












"""
for klasoryolu,klasorisimleri,dosyaisim in os.walk("C:/Users/tahaslı/Desktop/Python/calisma/15 - İleri Seviye Modüller/osmodulu/yeniklasorolusturmakistiyorum"):
    print("klasör yolu ",klasoryolu)
    print("klasör isim ",klasorisimleri)
    print("dosya isim ",dosyaisim)
    print("--------------------------------------------")
"""












"""
aaa = os.stat("y.txt").st_mtime
aaa = datetime.fromtimestamp(aaa)
print(aaa)
"""







"""
os.rename("x.txt","y.txt")
"""



"""
os.removedirs("deneme2/deneme3")
"""




"""
os.rmdir("deneme2")
"""









"""
print("Bulunduğumuz klasör:", os.getcwd())

os.rmdir("deneme2/deneme3")
"""







"""
print(os.getcwd())

os.makedirs("deneme2/deneme3")
"""










"""
print(os.getcwd())

os.mkdir("yeniklasorolusturmakistiyorum/deneme")"""
"""
yeniklasorolusturmakistiyorum klasörü altında deneme
adlı klasör oluşturduk.
"""









"""
print(os.getcwd())

os.mkdir("yeniklasorolusturmakistiyorum")
"""


"""
os.chdir("C:/Users/tahaslı/Desktop")
#print(os.listdir())

for i in os.listdir():
    print("-",i)
  """  