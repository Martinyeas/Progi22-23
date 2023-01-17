import random
import subset

fovarosok=["Bécs","Bern","Párizs","London"]
fovaros = None
while fovaros !='':
    print("fővárosok jelenleg:",",".join(fovarosok))
    fovaros = input("Kérek egy fővárost: ")
    if fovaros !="":
        fovarosok.append(fovaros)
n = random.randint(0,len(fovarosok))

for index,fovaros in enumerate(fovarosok):
    print(index,fovaros)

n = int(n)
print("A számítógép szerint ez a legszebb főváros:",fovarosok[n])

while len(fovarosok)>0:
    print("fővárosaink: ",",".join(fovarosok))
    melyik = input("Melyik főváros a legszebb?: ")
    if melyik in fovarosok:
        fovarosok.remove(melyik)
    else:
        print("Ilyen főváros nincs a listában.")