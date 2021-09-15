import sqlite3
con = sqlite3.connect("kutuphane.db")
cursor = con.cursor()

def tabloolustur(): #veritabanı tablo oluşturma
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik(isim text, yazar text, yayinevi text, sayfa_sayisi int)")
    con.commit() #işlemin taahhüt edilmesine yarar.

def deger_ekle(isim,yazar,yayinevi,sayfa_sayisi):
    cursor.execute("INSERT INTO kitaplik VALUES(?,?,?,?)",(isim,yazar,yayinevi,sayfa_sayisi))
    con.commit()

def verileri_al():
    cursor.execute("SELECT * FROM kitaplik")
    data = cursor.fetchall()
    for i in data:
        print(i)

def veriguncelle(eski_yayinevi,yeni_yayinevi):
    cursor.execute("UPDATE kitaplik SET yayinevi=? WHERE yayinevi=?",(yeni_yayinevi,eski_yayinevi))
    con.commit() #veritabanı güncellemesi gerektiğinde kullanılır.
    print("Başarıyla güncellendi.")
    
def verilerisil(ad):
    cursor.execute("DELETE FROM kitaplik WHERE isim=?",(ad,))
    con.commit()
    print(ad ," isimli kayıt başarı ile silindi.")

verilerisil("SucveCeza")
con.close()