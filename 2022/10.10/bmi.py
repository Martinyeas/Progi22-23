import math

bmi_lista_tomeg = []
bmi_lista_magassag = []
tomeg = "1"
magassag = "1"

while tomeg != "" and magassag != "":
    tomeg = input("Adja meg a testtömegét (kg): ")
    magassag = input("Adja meg a magasságát (cm): ")
    if tomeg != "" and magassag != "":
        bmi_lista_tomeg.append(int(tomeg))
        bmi_lista_magassag.append(int(magassag))
    else:
        break

bmi_lista_tomeg.sort()
bmi_lista_magassag.sort()
for i in range(0,len(bmi_lista_tomeg)):
    bmi = bmi_lista_tomeg[i]/math.pow(bmi_lista_magassag[i]/100,2)

    print(bmi)

    if bmi < 24.99 and bmi >18.5:
        print("Normális.")
    elif bmi > 24.99:
        print("Túlsúlyos.")
    else:
        print("Sovány.")