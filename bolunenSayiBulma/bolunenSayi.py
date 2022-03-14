print("Minumum sayiyi giriniz")
min_sayi = int(input())
print("Maksimum sayiyi giriniz")
max_sayi = int(input())
print("Sayilar kaça bölünebilir olsun")
bolunecek_sayi = int(input())
def bolunenSayiBulma (min_sayi,max_sayi,bolunecek_sayi):


    toplam_sayi = 0
    bolunen_sayilar = []

    for i in range(min_sayi,max_sayi):
        if(i % bolunecek_sayi == 0):
            bolunen_sayilar.append(i)
            toplam_sayi +=1
    print("Bölünen sayilar :")
    print(bolunen_sayilar)
    print("toplam sayi :")
    print(toplam_sayi)
bolunenSayiBulma(min_sayi,max_sayi,bolunecek_sayi)


