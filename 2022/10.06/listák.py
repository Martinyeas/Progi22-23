import enum


ps = [10,20,30,40]
qs = ["alma","eper","barack"]
print(ps)
print(qs)

zs = ["hello",2.0,5,[10,20]]
print(zs[3])
print(zs)

szotar = ["alma","sajt","kutya"]
szamok = [17,123]
ures_lista = []
print(szotar,szamok,ures_lista)

print(szamok[0])
for i in enumerate(szamok):
    print(i)

for (i,ert) in enumerate(szamok):
    szamok[i] = ert**2
    print(szamok[i])

for (i,v) in enumerate(["banan","alma"]):
    print(i,v)

sajat_lista = []
sajat_lista.append(6)
sajat_lista.append(20)
sajat_lista.append(9)
print(sajat_lista)

sajat_lista.insert(1,10)
print(sajat_lista)

sajat_lista.insert(0,16)
print(sajat_lista)

print(sajat_lista.count(16))

sajat_lista.extend([5,6,7])
print(sajat_lista)

print(sajat_lista.index(9))

sajat_lista.reverse()
print(sajat_lista)

sajat_lista.sort()
print(sajat_lista)

sajat_lista.remove(16)
print(sajat_lista)

szoveg_lista = ["barack","alma","mandarin"]
szoveg_lista.sort()
print(szoveg_lista)
szoveg_lista2 = ["én","te","ő","mi","ti","ők"]
szoveg_lista2.sort()
print(szoveg_lista2)