# Kullanıcıdan iki sayı alınır
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

# İşlem seçimi için kullanıcıya mesaj gösterilir
print("İşlem seçin:")
print("1 - Toplama")
print("2 - Çıkarma")
tercih = input("Tercihinizi yapın (1 veya 2): ")

# İşlem tercihine göre hesaplama yapılır
if tercih == "1":
    sonuc = sayi1 + sayi2
    islem = "toplama"
elif tercih == "2":
    sonuc = sayi1 - sayi2
    islem = "çıkarma"
else:
    print("Geçersiz tercih!")
    exit()

# Sonucu ekrana yazdırma
print(f"Sonuç: {sonuc} ({sayi1} ile {sayi2} {islem} sonucu)")

