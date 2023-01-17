vnev = None
vonalk = None
vonalkodnemmagyar = 600

def logika(szam):
    if vonalk < vonalkodnemmagyar:
        return True
    else:
        return False

while True:
    vnev = input("Adja meg a vásárló nevét! ")
    if vnev == "":
        break
    vonalk = int(input("Add meg a gyümölcs vonalkódjának első három számát! "))
    if logika(vonalk):
        print(f"{vnev} magyar gyümölcsöt vásárolt.")
    else:
        print(f"{vnev} nem magyar gyümölcsöt vásárolt.")