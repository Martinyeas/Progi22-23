literek = 0
maximum = 3.5
jo = 2.5
napi_teljesítve = False
elmondta = False

while literek < 3.5:
    deci = int(input("Hány deci vízet ivott? "))
    literek = deci/100 + literek
    print(literek," l vizet ivott.")
    if literek >= jo:
        napi_teljesítve = True
        if not elmondta:
            print("Megitta a napi célt!:) ")
            elmondta = True
        if literek >= maximum:
            print("Viszlát!")
            break