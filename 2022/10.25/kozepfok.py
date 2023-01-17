nev = input("Add meg a jelentkező nevét! ")
pont = int(input("Hány centiméter magas? "))

while nev == "":
    nev = input("Add meg a jelentkező nevét! ")

if pont >= 170:
    print(f"{nev} vizsga szintje nem középfokú.")
elif pont < 170 and pont >= 150:
    print(f"{nev} vizsga szintje középfokú.")