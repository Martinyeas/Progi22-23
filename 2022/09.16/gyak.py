barack = int(input("Hány barack termett? "))
barack_ár = int(input("Mennyi a barack ára? "))

körte = int(input("Hány körte termett? "))
körte_ár = int(input("Mennyi a körte ára? "))

if barack < 10:
    bminősítés = "kevés"
elif barack > 20:
    bminősítés = "sok"
else:
    bminősítés = "jó"

if körte < 10:
    kminősítés = "kevés"
elif körte > 20:
    kminősítés = "sok"
else:
    kminősítés = "jó"

if barack_ár < 790:
    bárminősítés = "kevés"
elif barack_ár > 900:
    bárminősítés = "sok"
else:
    bárminősítés = "jó"

if körte_ár < 790:
    kárminősítés = "kevés"
elif körte_ár > 900:
    kárminősítés = "sok"
else:
    kárminősítés = "jó"

print(f"barakc egy {bminősítés} és {bárminősítés} az ára")
print(f"körte egy {kminősítés} és {kárminősítés} az ára")