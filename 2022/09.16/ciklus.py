from itertools import repeat
import math,cmath

a = float(input("Kérem a másodfokú egyenlet főegyütthatóját: "))

while a == 0:
    print("Ez nem lesz másodfokú egyenlet; nem oldom meg.")
    a = float(input("Kérem a másodfokú egyenlet főegyütthatóját: "))

b = float(input("Kérem az elsőfokú tag együtthatóját: "))
c = float(input("Kérem a konstans tagot: "))

d = b*b-4*a*c
print("A diszkrimináns értéke: ",d)

if d>=0:
    print("Van valós megoldás.")
    