import time
import random
import numpy as np

def para():
    print('Ne kadar para yatırmak istersiniz')
    tutar=int(input('Para (TL) :'))
    print('Güncel Bakiyeniz : ,tutar')
    return tutar

def bakiye():
    while True:
        bakiye = 10000
        kullanici_adi = input("Lütfen Kullanici Adinizi Giriniz:")
        time.sleep(1)
        sifre = input("Sifrenizi giriniz")
        time.sleep(1)
        if kullanici_adi == "BüyükKumar" and sifre == "iyiolankazansın":
            print("Hosgeldiniz:", kullanici_adi)
            print("Bakiyeniz:", bakiye)
            return bakiye
            break
        else:
            print("Kullanici Adi veya Sifre Yanlis! Tekrar deneyiniz")

def Online_Oyna():
    print("Big Boss Sayfasina Yönlendiriliyorsunuz! ")
    print("lütfen ilgili Linke Tiklayiniz: ")
    print("www.bigBoss.com")
Online_Oyna()

print("BigBoss'a Hos Geldiniz")
time.sleep(1)
print("""
1.Online Oyna 
2.Bakiyen ile Oyna

 """)
time.sleep(1)

veri = input("Seciminiz: ")

def zar():
  print("Zariniz Atiliyor!")
  time.sleep(1)
  oyuncu_zari=np.random.randint(1,7,2)
  sum_oyuncu=sum(oyuncu_zari)
  print("Zarlarinizin toplami",sum(oyuncu_zari))
  time.sleep(1)
  print("\n")
  print("Sira Bilgisayarda")
  time.sleep(1)
  print("Zar atiliyor...")
  time.sleep(1)
  bilgisayar=np.random.randint(1,7,2)
  sum_bilgisayar=sum(bilgisayar)
  print("Bilgisayar Zar toplami:",sum_bilgisayar)
  return sum_oyuncu,sum_bilgisayar


def oyna():
    print("BigBoss'a Hos Geldiniz")
    time.sleep(1)
    print("""
  1.Canlı Para ile Oyna
  2.Mevcut Bakiyen Ile Oyna
  3-Online Oyna
  4-Arkadaşlarından para iste
  5-Sistemden borç al
  4-Masayi Terket

  """)
    time.sleep(1)

    veri = input("Seciminiz: ")


user = 0
system = 0
i = 0
while i < 5:

    if veri == "1":
        para()
        a, b = zar()
        if a > b:
            score = +1

            print("Tebrikler Büyük Kazandin")
            print("Yeni bakiyeniz:", para() + 5)
            print(f'Puaniniz:{user} bilgisayar{score}')
        elif a < b:
            system += 1
            print("Kaybettiniz:(")
            print("Kalan Bakiye", para() - 5)
        else:
            print("Beraberlik")
    elif veri == "2":
        bakiye()
        a, b = zar()

        if a > b:
            score = +1
            print("tebrikler Kazandiniz")
            print("Yeni bakiyeniz:", para() + 5)

        elif a < b:
            system += 1
            print("Kaybettiniz:(")
            print("Kalan Bakiye", para() - 5)
        else:
            print("Beraberlik")
    elif veri == "3":
        Online_Oyna()
    else:

        print("iyi günler dileriz")
        break

oyna()