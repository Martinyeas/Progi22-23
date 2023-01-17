def fuggveny(letszam):
    if letszam > 1000:
        return True
    else:
        return False

while True:
    iskolanev = input("Add meg az iskola nevét! ")
    letszam = int(input("Add meg a pontszámát! "))
    if iskolanev == "":
        break
    if fuggveny(letszam):
        print(f"{iskolanev} nagy létszámú iskola.")
    else:
        print(f"{iskolanev} kis létszámú iskola.")