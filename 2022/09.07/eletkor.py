import time

nev = input("Kérem adja meg a nevét ")
print(nev)
ÉV=2022
udv = (f'Üdvözöllek {nev}')
print(udv,"szép napot kívánok neked", sep = " ")
eletkor = int(input("Kérem adja meg a születési évét "))
eletk = ÉV -eletkor

if eletk > 7 and eletk < 15:
    print("Általános iskolás")
elif eletk > 14 and eletk < 20:
    print("Közép iskolás")
else:
    print("Felnőtt")