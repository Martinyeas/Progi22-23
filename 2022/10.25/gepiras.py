nev = "nil"

def mgfll(gepel):
    if gepel < 60:
        print(f"{nev} felvételt nyert.")
    else:
        print(f"{nev} nem nyert felvételt.")

while nev != "":
    nev = input("Add meg a jelentkező nevét! ")
    if nev != "":
        gepel = int(input("Hány szót tud gépelni 1 perc alatt? "))
        mgfll(gepel)