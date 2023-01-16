#Kérje be két hajó sebességét és adja meg, melyik gyorsabb
hajo1 = int(input("Adja meg az egyik hajó sebességét! "))
hajo2 = int(input("Adja meg a másik hajó sebességét! "))
csomokm = 1.82

def atalakit(sebesseg):
    return sebesseg * 1.852

if hajo1 > hajo2:
    print("Az első hajó gyorsabb mint a másik!")
elif hajo1 < hajo2:
    print("A második hajó gyorsabb mint az első!")
else:
    print("Egyenlő gyorsak!")
print(atalakit(hajo1))
print(atalakit(hajo2))