# Soru 1 Ekranda “Hello World” yazdıran python örneği
print("Hello World")

# Soru 2 Kullanıcının ismini alarak “Merhaba (kullanıcı ismi)” yazdıran python örneğ
isim = input("İsminizi giriniz:")
print("Hello",isim)

# Soru 3  Girilen 2 sayıyı toplayan python örneği
sayi1 = input("Toplanacak ilk sayıyı giriniz:")
sayi2 = input("Toplanacak ikinci sayıyı giriniz:")
toplam = int(sayi1) + int(sayi2)
print("Sayıların toplamı: ",toplam)

# Soru 4 Girilen 2 sayının ortalamasını bulan python örneği
sayi1 = input("Birinci sayıyı giriniz:")
sayi2 = input("İkinci sayıyı giriniz:")
ort = (int(sayi1)+int(sayi2))/2
print(f"Ortalamanız: {ort}")

# Soru 5 Klavyeden girilen vize ve final notuna göre vizenin %40 ve finalin %60’ını alan ve sonucu ekranda gösteren python kodunu yazınız.
vize = input("Vize notunuzu giriniz:")
final = input("Final notunuzu giriniz:")
ort = (int(vize)*0.4 + int(final)*0.6)/2
print(f"Vize notunuz {vize}, final notunuz {final}, ortalamanız ise {ort}")