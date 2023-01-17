F = int(input("Adjon meg egy hőfokot: "))
OP = 1539
FP = 2750

if OP < FP:
    if F>= OP and F < FP:
        print("A vas olvadáspontja")
    elif F>= FP:
        print("A vas forráspontja")
    elif F> FP+10:
        print("A vas gáz")
    else:
        print("A vas szilárd")
