nev = None
pont = None
nevek = []
pontok = []

while nev != "" or nev != "":
    nev = str(input("Add meg a vizsgázó nevét! "))
    if nev == "" or nev == "":
        break
    pont = int(input("Add meg a pontszámát "))
    nevek.append(nev)
    pontok.append(pontok)
    if pont >= 100:
        print(f"{nev} vizsgája sikeres.")
    else:
        print(f"{nev} vizsgája sikertelen.")
