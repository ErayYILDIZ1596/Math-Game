import time
import random

birincisayilar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

ikincisayilar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]

islemler = ["÷", "+", "-", "x"]

print("""           Matematik oyunu""")
time.sleep(1)
print("""     Matematik oyununa hoş geldiniz!""")
time.sleep(2)
print("""Bu oyunda alt tarafta bir işlem verilecek ve bu işlemi 10 saniye içerisinde yapamazsanız kaybedeceksiniz""")
time.sleep(5)

for i in range(1):
    baslangic = input("Başlamak ister misiniz?:")
    if baslangic == "evet":
        
        
        a = random.choice(birincisayilar)

        b = random.choice(ikincisayilar)

        c = random.choice(islemler)

        sonuc = input(a, c, b)
        start_time = time.time()
        time.sleep(10)
        end_time = time.time()
        sonzaman = end_time - start_time
        print("Son zamanınız:", sonzaman)
        if c == "x":
            if sonuc == a*b and sonzaman < 10:
                print("Kazandınız!")
            else:
                print("Zamanınız bittiği için veya cevabınız yanlış olduğu için kaybettiniz!")

        if c == "÷":
            if sonuc == a/b and sonzaman < 10:
                print("Kazandınız!")
            else:
                print("Zamanınız bittiği için veya cevabınız yanlış olduğu için kaybettiniz!")

        if c == "+":
            if sonuc == a+b and sonzaman < 10:
                print("Kazandınız!")
            else:
                print("Zamanınız bittiği için veya cevabınız yanlış olduğu için kaybettiniz!")

        if c == "-":
            if sonuc == a-b and sonzaman < 10:
                print("Kazandınız!")
            else:
                print("Zamanınız bittiği için veya cevabınız yanlış olduğu için kaybettiniz!")
    else:
        break
