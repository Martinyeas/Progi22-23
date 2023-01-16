ido = int(input("Hány óra van most? "))
zaras = 16
nyitas = 8
if ido < zaras and ido > nyitas:
    print("A bolt nyitva van")
    print(f"Ennyi órád van még odaérni: {zaras-ido}")
else:
    print("A bolt zárva van")