# Soru 1 1-100 Arası Sayıları Ekranda Listele
for i in range(1,101):
    print(i)

# Soru 2  1-100 arası Çift Sayıları Listele
for i in range(1,101):
    if(i%2==0):
        print(i)

# Soru 3 1-100 Arası Tek Sayıları Listele
for i in range(1,101):
    if(i%2==1):
        print(i)

# Soru 4 1-100 Arası 3′ e ve 5′ e tam bölünen sayıları bul
for i in range(1,101):
    if(i%3==0 and i%5==0):
        print(i)        

# Soru 5 1'den Kullanıcının Girdiği Sayıya Kadar Sayıları Listele
kullanici = int(input("Bir sayı giriniz:"))
for i in range(1,kullanici+1):
    print(i)
    
# Soru 6 Kenarları Girilen Dikdörtgenin Alanı ve Çevresini Bul
uzunk=int(input("Uzun kenarı giriniz:"))
kisak=int(input("Kısa kenarı giriniz:"))
alan = uzunk*kisak
cevre = 2*(uzunk+kisak)
print(f"Alan:{alan}, Cevre:{cevre}")

# Soru 7 Girilen metnin harflerini alt alta yazdır
kullanici = input("Bir kelime giriniz:")
sayac=0
while(sayac<len(kullanici)):
    print(kullanici[sayac])
    sayac+=1

# Soru 8 Kullanıcıya sinema ya da tiyatro tercihi sorulsun. 
# Sinema izlemek için 15 TL, tiyatro için 10 TL ödenmesi gerekmedir.
# Öğrencilere %50 indirim yapıldığı düşünülerek öğrenci ise indirim yapılan; 
# öğrenci değilse indirimsiz tutarı hesaplayarak ekrana yazdıran kodu yaz.

musteri = input("Sinema izlemek için [1], Tiyatro izlemek için[2]:")
ogrenciMi = input("Öğrenci misiniz[T/F]:")
sinemafiyat = 15
tiyatrofiyat = 10

if(musteri=="1"):
    if(ogrenciMi=="T"):
        print(f"Ödeyeceğiniz tutar:{sinemafiyat-sinemafiyat*1/2}")
    else:
        print(f"Ödeyeceğiniz tutar:{sinemafiyat}")    
elif(musteri=="2"):
    if(ogrenciMi=="T"):
        print(f"Ödeyeceğiniz tutar:{tiyatrofiyat-tiyatrofiyat*1/2}")
    else:
        print(f"Ödeyeceğiniz tutar:{tiyatrofiyat}")

else:
    print("Hatalı seçim yaptınız.")        

# Soru 9 Girilen Sayının Asal Sayı mı Değil mi olduğunu bul
sayi = int(input("Bir sayı giriniz:"))
toplam=0
for i in range(2,sayi):
    if(sayi%i==0):
        toplam+=1

if(toplam==0):
    print(f"Girilen sayı asaldır,{toplam} tane pozitif böleni vardır.")
else:
    print(f"Girilen sayı asal değildir,{toplam} tane pozitif böleni vardır.")     

# Soru 10 1 den kullanıcının girmiş olduğu sayıya kadar olan tek ve çift sayıların toplamını ayrı ayrı bulan ve sonucu ekranda göster.
kullanici = int(input("Bir sayı giriniz:"))
tektoplam = 0
cifttoplam = 0
for i in range(1,kullanici):
    if(i%2==0):
        cifttoplam+=i
    elif(i%2==1):
        tektoplam+=i

print(f"Tek sayıların toplamı:{tektoplam}")
print(f"Çift sayıların toplamı:{cifttoplam}")            

# Soru 11  Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda göster
maas = int(input("Maaşı giriniz:"))
zamoran = int(input("Zam oranını giriniz:"))
zamlimaas = maas + maas*zamoran/100
print(f"Zam almadan önceki maaş:{maas}")
print(f"Zamlı maaş:{zamlimaas}")
