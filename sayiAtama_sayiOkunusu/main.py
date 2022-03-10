
onlukDictionary = ["on","yirmi","otuz","kırk","elli","altmış","yetmis","seksen","doksan"]
birlikDictionary = ["bir","iki","uc","dort","bes","altı","yedi","sekiz","dokuz"]
def sayiOkunusu(okunacakSayi):
    print(onlukDictionary[int(okunacakSayi/10)-1] + " "+ birlikDictionary[int(okunacakSayi % 10)-1])

def sayiAtama(sayi):
    if(sayi<10 or sayi>99):
        print("Sayi ilgili değer aralığında değil")
        exit(1)
    okunacakSayi = sayi
    sayiOkunusu(okunacakSayi)

def main():
    print("Okunacak sayiyi giriniz :")
    sayi = int(input())
    sayiAtama(sayi)


if __name__ == '__main__':
    main()