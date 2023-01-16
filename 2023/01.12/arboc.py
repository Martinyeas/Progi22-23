magassag = int(input("Adja meg az árbóc magasságot centiméterben: "))

def atvaltas(centimeter):
    return centimeter/100

print(f"Méterben: {atvaltas(magassag)}")

nev = input("Kapitány nevét adja meg! ")
print(nev.capitalize())