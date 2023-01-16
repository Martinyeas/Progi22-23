hajo1 = int(input("Adja meg az egyik hajó sebességét! "))
hajo2 = int(input("Adja meg a másik hajó sebességét! "))
csomokm = 1.82

def atalakit(sebesseg):
    return sebesseg * 1.852

print(atalakit(hajo1))
print(atalakit(hajo2))