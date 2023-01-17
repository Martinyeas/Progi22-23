import random

def nevelo(szo):
    maganhangzok=["a","á","e","é","i","í","o","ó","ö","ő","u","ú","ü","ű"]
    isin = False
    for i in range(0,len(maganhangzok)):
        if i == szo[0].lower:
            isin = True
            print(szo[0])
            break
    if isin:
        return "az"
    else:
        return "a"

def jelzo():
    return random.choice(["piros","nagy","könnyed","almafa"])

szo = jelzo()
print(f"{nevelo(szo)} {szo}")