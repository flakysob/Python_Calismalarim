import sqlite3
con = sqlite3.connect("kutuphane.db")
cursor = con.cursor()

def tabloolustur(): #veritabanı tablo oluşturma
    cursor.execute("create table if not exists kitaplik(isim text, yazar text, yayinevi text, sayfa_sayisi int)")
    con.commit() #işlemin taahhüt edilmesine yarar.

def deger_ekle(isim,yazar,yayinevi,sayfa_sayisi):
    cursor.execute("insert into kitaplik values(?,?,?,?)",(isim,yazar,yayinevi,sayfa_sayisi))
    con.commit()

def verileri_al():
    cursor.execute("select * from kitaplik")
    data = cursor.fetchall()
    for i in data:
        print(i)

def veriguncelle(yayine):
    cursor.execute("update kitaplik set yayinevi=? where yayinevi=?",("x",yayine))
    con.commit()

veriguncelle("Deneme")

con.close()