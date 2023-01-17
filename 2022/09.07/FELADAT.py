NEV = str(input("Kérem adja meg a nevét "))
AUTO_MARKA = str(input("Kérem adja meg a kedvenc autó márkáját "))
GYARTO_ORSZAG = str(input("Kérem adja meg a "+AUTO_MARKA+" gyártó országát "))
VEGSEBESSEG = int(input("Kérem adja meg a "+AUTO_MARKA+" végsebességét "))


TABLAZAT = [NEV,AUTO_MARKA,GYARTO_ORSZAG,VEGSEBESSEG]

print("{g} vidékein készül {a}, aminek {v} km/h a végsebessége".format(g=GYARTO_ORSZAG,a=AUTO_MARKA,v=VEGSEBESSEG))
for i in TABLAZAT:
    print(i)

print(f'{GYARTO_ORSZAG=}, {AUTO_MARKA=}, {VEGSEBESSEG=}')