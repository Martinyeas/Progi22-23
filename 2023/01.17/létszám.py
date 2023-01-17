egyik = int(input("Adj meg az egyik iskolai számot! "))
masik = int(input("Adjon meg egy másik iskolai számot! "))

if egyik > masik:
    print(f"A létszám érték az egyik iskolában több, {egyik}")
elif egyik < masik:
    print(f"A létszám érték az másik iskolában több, {masik}")
else:
    print(f"A két létszám egyenlő")
