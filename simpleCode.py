
import sqlite3

connection = sqlite3.connect("kutuphane.db")
cursor     = connection.cursor()

def tablo_olustur():
    cursor.execute("create table if not exists kitaplık (İsim text,Yazar text,Yayınevi TEXT,Sayfa_Sayisi INT)")
    connection.commit()

def veri_ekle():
    cursor.execute("insert into kitaplık Values('İstanbul Hatırası','Ahmet Ümit','Everest','561')")
    connection.commit()

def veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı):
    # execute methodu için özel formatlama tuple cinsinden
    cursor.execute("insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    connection.commit()


isim = input("İsim : ")
yazar = input("Yazar : ")
yayınevi = input("Yayınevi : ")
sayfa_sayısı = int(input("Sayfa Sayısı : "))
veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı)

connection.close()