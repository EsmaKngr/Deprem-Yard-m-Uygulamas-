kullanici = {}
bagis_kaydet = {}

def uyeol():
    ad = input("Adınızı giriniz. ")
    soyad = input("Soyadınızı giriniz. ")
    telefonno = input("Telefon numaranızı giriniz. ")
    
    if len(telefonno)==10:
        print("geçerli telefon numarası.")
    else:
        print("geçersiz telefon numarası.")
            
    kullanici_adi = input("Kullanıcı adı belirleyin: ")
    sifre = input("Şifrenizi belirleyin")

    kullanici[kullanici_adi] = {
        "ad": ad,
        "soyad": soyad,
        "telefon": telefonno,
        "sifre": sifre            }
    print("Kaydınız tamamlandı.")

def calisangirisi():
    calisan_no = print("Çalışan numaranızı giriniz.")
    if calisan_no==1709911:
            print("Doğru çalışan no")
    else:
        print("Çalışan no yanlış.")
        
    calisan_sifre = print("Çalışan şifrenizi giriniz.")
    
    

def girisyap():
    kullanici_adi = input("Kullanıcı adınızı giriniz: ")
    sifre = input("Şifrenizi giriniz: ")

    if kullanici_adi in kullanici and sifre:
        print("Giriş başarılı.")
    else:
        print("girilen bilgiler yanlış.")
        
    miktar = float(input("Bağış miktarını girin: "))
    
    if miktar >= 1000:
        mesaj = "Çok teşekkür ederiz! Cömert bağışınız için minnettarız."
    elif miktar >= 500:
        mesaj = "Teşekkür ederiz! Bağışınız gerçekten değerli."
    elif miktar >= 200:
        mesaj = "Bağışınız için teşekkürler! Destekleriniz bizim için önemli."
    else:
        mesaj = "Bağışınız için teşekkür ederiz!"
    
    print("Bağış kaydedildi.",mesaj)
#bagis_kaydet("bagislar.txt",)
   
   


def sifremi_unuttum():
    kullanici_adi = input("Kullanıcı adınızı giriniz. ")
    telefonno = input("Telefon numaranızı giriniz.")


    if kullanici_adi in kullanici:
        yeni_sifre = input("Yeni şifrenizi belirleyin: ")
        kullanici[kullanici_adi]["sifre"] = yeni_sifre
        print("Yeni şifreniz başarıyla kaydedildi.")
    else:
        print("Geçersiz kullanıcı adı.")
        


x=1
while x==1 :
    print("Deprem Yardım Uygulaması")
    print("1-Sisteme üye olma")
    print("2- Sisteme giriş yap")
    print("3- Şifremi Unuttum")
    print("4- Çalışan girişi")
    print("0- Çıkış")
    
    secim = input("Yapmak istediğiniz işlemi giriniz")

    if secim == "1":
        uyeol()
    elif secim == "2":
        girisyap()
        
    elif secim == "3":
        sifremi_unuttum()
    elif secim=="4":
        calisangirisi()
    elif secim == "0":
        break
    else:
        print("Böyle bir seçenek bulunmamaktadır tekrar deneyiniz.")
        
        
        

