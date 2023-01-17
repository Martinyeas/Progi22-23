v = 40

for i in range(1,v):
    if i %3 == 0:
        print(i)

szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
for i in range(0,len(szavak)):
    if szavak[i][0].capitalize() == "T":
        print(szavak[i])
lisat = []
szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
for i in range(0,len(szavak)):
    if szavak[i][0].capitalize() == "T":
        lisat.append(szavak[i])
print(lisat)
szamok = [120, 9, 5, 24, 6, 17, -45, 92, 15, 48, 57]
for i in range(1,len(szamok)):
    if i %3 == 0 and i %2 == 0:
        print(i)