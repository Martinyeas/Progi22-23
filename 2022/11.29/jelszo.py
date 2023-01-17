nev = "BORI"
jelszo = "szivecske"

jo = False
while not jo:
    nevk = input("Adja meg a felhasználónevét! ")
    jelszok = input("Adja meg a jelszavát! ")
    if nevk == nev:
        if jelszok == jelszo:
            jo = True
            break
        else:
            print("Belépés megtagadva.")
    else:
        print("Belépés megtagadva.")
print("Belépés engedélyezve.")