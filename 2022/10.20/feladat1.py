import random


a = 0
while a < 10:
    if a % 2 == 0:
        print(a)
    a+=1
b = 10
while b > 0:
    print(b)
    b-=1
c = 10
while c > 0:
    if not c % 2 == 0:
        print(c)
    c-=1

szoveg = input("Adjon meg egy szöveget: ")
szor = int(input("Adjon meg egy kívánt számot: "))
print(szoveg*szor)

szam = 3
while szam % 2 != 0:
    szam = int(input("Adjon meg egy páros számot: "))

lepes = 0
harmas = 0
while lepes < 20+1:
    lepes +=1
    randszam = random.randint(1,12)
    if randszam % 3 == 0:
        print(randszam,end="")
        harmas +=1
print("Ennyi hármas szám volt:",harmas)
