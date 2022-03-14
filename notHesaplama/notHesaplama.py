vize1 = input("1. Vize:")
if (0<=vize1<=100):
    exit()
vize2 = input("2. Vize:")
Final = input("Final:")

sonuc = int(vize1) * (3 / 10) + int(vize2) * (3 / 10) + int(Final) * (4 / 10)

if (sonuc>=90):
    print("AA")
elif (sonuc<90 and sonuc>=85):
    print("BA")
elif (sonuc<85 and sonuc>=80):
    print("BB")
elif (sonuc<80 and sonuc>=75):
    print("CB")
elif (sonuc<75 and sonuc>=70):
    print("CC")
elif (sonuc<70 and sonuc>=65):
    print("DC")
elif (sonuc<65 and sonuc>=60):
    print("DD")
elif (sonuc<60 and sonuc>=55):
    print("FD")
else :
    print("FF")
