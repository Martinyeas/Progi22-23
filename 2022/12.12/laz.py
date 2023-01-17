def laz(homerseklet,beteg):
    if homerseklet < 38:
        return (f"{beteg} nem lázas.")
    else:
        return (f"{beteg} lázas.")

while True:
    beteg = str(input("Adja meg a beteg nevét! "))
    if beteg == "":
        break
    homerseklet = int(input("Adja meg a beteg nevét! "))
    print(laz(homerseklet,beteg))