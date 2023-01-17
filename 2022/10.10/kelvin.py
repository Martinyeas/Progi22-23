
c_lista = []

for _ in range(0,3):
    c_lista.append(int(input("Mi a jelenlegi hőmérséklet?(C*) ")))

for i in c_lista:
    kelvin = i-273
    print(kelvin)
    if i < 21 and i >16:
        print("A hőmérséklet megfelelő.")
    elif i > 21:
        print("Meleg van.")
    else:
        print("Hideg van.")