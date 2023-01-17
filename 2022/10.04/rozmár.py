ossz = 0

while ossz <= 35 and (ivas:=int(input("Hány decit ittál? "))):
    print(f'Már {(ossz:=ossz+ivas)/10:3.1f} litert ittál.')
    if ossz >= 25:
        print("Már elérted a 2.5 litert")
print('béke a hasadba\'!')