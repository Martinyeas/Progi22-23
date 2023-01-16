visszaszamlal = int(input("Hány órás visszaszámlálást tervezünk? "))
ido = visszaszamlal
while visszaszamlal > 0:
    print(visszaszamlal)
    valasztas = input("Fel kell függeszteni a visszaszámlálást(i/n)? ")
    if valasztas == "n":
        visszaszamlal -=1
    elif valasztas == "i":
        ido +=1
        visszaszamlal -=1

print(f"A rakéta a visszaszámlálást követően ennyi órával indult: {ido}")