# Soru 1 Yazılı Ortalaması Girilen Öğrencinin Sınıf Geçme Durumunu (GEÇTİ – KALDI) göster
ortalama = int(input("Ortalamanızı giriniz:"))
if(ortalama>50):
    print(f"Tebrikler dersi {ortalama} ortalama ile geçtiniz.")
else:
    print(f"Maalesef dersten {ortalama} ortalama ile kaldınız.")    

# Soru 2 Girilen Sayının Tek mi Çift mi Olduğunu bul
sayi = int(input("Bir sayı giriniz:"))
if(sayi%2==0):
    print(f"Girdiginiz {sayi} sayısı çifttir.")
else:
    print(f"Girdiginiz {sayi} sayısı tektir.")    


# Soru 3 Girilen Sayının Pozitif, Negatif, ya da 0 Olduğunu Bul
sayi = int(input("Bir sayı giriniz:"))

if(sayi>0):
    print(f"{sayi} pozitiftir.")
elif(sayi<0):
    print(f"{sayi} negatiftir.")
else:
    print(f"{sayi} sıfıra eşittir.")    


# Soru 4 Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ=ağırlık/(boy*boy), boymetre cinsinden verilmeli) hesaplayınız.
#VKİ 18 ile < 25 aralığındaysa normal, VKİ 25 ile <30 aralığındaysa kilolu, VKİ 30 ve daha yüksekse obez, VKİ 35 ve daha fazlaysa ciddi obez olarak kabul edilir. VKİ’ni hesaplayarak kişinin durumunu yazdırınız.
boy = float(input("Boyunuzu giriniz(mt):"))
kilo = int(input("Kilonuzu giriniz:"))
vki = kilo/(boy*boy)
if vki>18 and vki<25:
    print(f"Vücut kitle endeksiniz {vki}. Siz normal bir bireysiniz.")
elif vki>25 and vki<30:
    print(f"Vücut kitle endeksiniz {vki}. Siz kilolu bir bireysiniz.")
elif vki>=30:
    print(f"Vücut kitle endeksiniz {vki}. Siz obez bir bireysiniz.")  
elif vki>=35:
    print(f"Vücut kitle endeksiniz {vki}. Siz ciddi obez bir bireysiniz.") 
else:
    print("Girdiginiz boy ve kilo değerlerini gözden geçiriniz.")      


# Soru 5 Yaşı Girilen Kişinin Ehliyet Alıp Alamayacağını Göster
yas = int(input("Yaşınızı giriniz:"))
if yas>18:
    print(f"Tebrikler! Yaşınız {yas} olduğu için ehliyet alabilirsiniz.")  
else:
    print(f"Maalesef! Yaşınız {yas} olduğu için ehliyet alamazsınız.")

