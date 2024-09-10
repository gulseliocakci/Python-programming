# bankamatik uygulaması
accountInfo = {
    "username" : "username",
    "password" : "12345",
    "totalMoney" : 20000,
    "ekHesapBakiyesi" : 10000
}
def bankAccount(islem):
    if(islem == 1):
        islem1()
    elif(islem == 2):
        islem2()
    elif(islem == 3):
        islem3()
    else:
        print("Yanliş bir sayi yazdiniz yeniden deneyiniz.")    

def islem1():
    print("Çekmek istediğiniz miktari yaziniz: ")
    cekilenPara = int(input())
    if(cekilenPara > accountInfo["totalMoney"]):
        print("Hesabinizda yeterli bakiye bulunmamaktadir.")
        print("Ek hesabinizdaki paradan kullanilmasini ister misiniz evet ya da hayir olarak belirtiniz.")
        onay = input().lower()
        if(onay == "evet"):
            cekilecekFazlaPara= cekilenPara - accountInfo["totalMoney"]
            if(cekilecekFazlaPara <= accountInfo["ekHesapBakiyesi"]):
                accountInfo["totalMoney"] = 0
                accountInfo["ekHesapBakiyesi"] = accountInfo["ekHesapBakiyesi"] - cekilecekFazlaPara
                print("Paranizi bölmeden alabilirsiniz.")
            else:
                print("Ek hesabinizdaki para yeterli olmadiği için işlem gerçekleştirilemiyor.")
        elif(onay == "hayır" or onay == "hayir"):
            print("İşlemlerinize devam edebilirsiniz.")
        else:
            print("Yazdiğiniz yanit geçersiz.")
    else:
        accountInfo["totalMoney"] = accountInfo["totalMoney"] - cekilenPara
        print("Paranizi bölmeden alabilirsiniz.")
def islem2():
    print("Güncel bakiyeniz: " + str(accountInfo["totalMoney"]))
    print("Ek hesap bakiyeniz: " + str(accountInfo["ekHesapBakiyesi"]))
def islem3():
    print("Yatirmak istediğiniz para miktarini yaziniz ve bölmeye parayi koyunuz: ")
    yatirilanPara = int(input())
    if(yatirilanPara > 0):
        accountInfo["totalMoney"] = accountInfo["totalMoney"] + yatirilanPara
    else:
        print("Yanliş bir değer yazdiniz.")
while(True):
    kullaniciAdi = input("Hosgeldiniz kullanici adinizi yaziniz: ").lower()
    sifre = input("Şifrenizi yaziniz: ").strip().lower()
    if(kullaniciAdi != accountInfo["username"] or sifre != accountInfo["password"]):
        print("Kullanici adi veya şifre hatali yeniden deneyiniz.")
    kontrol = kullaniciAdi == accountInfo["username"] and sifre == accountInfo["password"]
    while(kontrol):
        print("Yapmak istediğiniz işlemi seçiniz (işlemi belirten numarayi yaziniz. )")
        print("1) Para çekme")
        print("2) Bakiye sorgulama")
        print("3) Para yatirma")
        print("4) İşlemi sonlandirma")
        islem = int(input())
        if(islem ==1 or islem ==2 or islem ==3):
            bankAccount(islem)
        elif(islem == 4):
            break
        else:
            print("Yanliş bir sayi yazdiniz. yeniden deneyiniz.")