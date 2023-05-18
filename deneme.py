# Kullanıcıdan iki sayı alınması
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

# İşlem seçimi
print("Yapmak istediğiniz işlemi seçin:")
print("1 - Toplama")
print("2 - Çıkarma")
print("3 - Çarpma")
print("4 - Bölme")
secim = int(input("Seçiminizi yapın (1-4): "))

# İşlemi gerçekleştirme ve sonucu gösterme
if secim == 1:
    sonuc = sayi1 + sayi2
    print("Toplama sonucu:", sonuc)
elif secim == 2:
    sonuc = sayi1 - sayi2
    print("Çıkarma sonucu:", sonuc)
elif secim == 3:
    sonuc = sayi1 * sayi2
    print("Çarpma sonucu:", sonuc)
elif secim == 4:
    sonuc = sayi1 / sayi2
    print("Bölme sonucu:", sonuc)
else:
    print("Geçersiz bir seçim yaptınız.")
