
bejutott = False

while not bejutott:
    felhasznalonev = input("Kérem adja meg a felhasználónevét ")
    jelszo = input("Kérem adja meg a jelszavát ")
    if felhasznalonev == "bori69" and jelszo == "abc":
        bejutott = True
        print("Belépés sikeres.")
    else:
        print("Belépés sikertelen.")