nev = "n"

def mgfll(magassag):
    if magassag >= 170:
        print(f"{nev} megfelelő magasságú.")
    else:
        print(f"{nev} magassága nem megfelelő modellnek.")

while nev != "":
    nev = input("Add meg a jelentkező nevét! ")
    if nev != "":
        magassag = int(input("Hány centiméter magas? "))
        mgfll(magassag)