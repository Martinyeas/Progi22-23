liba = [2,4,7,9,8,5,4,3]
print(sum(liba))
osszeg = 0
for x in range(0,len(liba)):
    osszeg = osszeg + liba[x]
print(osszeg)
print(liba)

tomeg = 0
for i in range(0,len(liba)):
    tomeg = tomeg + i
print(tomeg)

tobb = 0
for i in range(0,len(liba)):
    if liba[i] > 3:
        tobb +=1
print(tobb)

van5kilos = False
kilos5 = 0
for i in range(0,len(liba)):
    if liba[i] >=5:
        kilos5 +=1
        van5kilos = True
if van5kilos:
    print("Van 5 kilós")
    print(kilos5,"db")

ujlibak = [3,5,7,5,7,4]
for x in range(0,len(ujlibak)):
    liba.append(ujlibak[x])
print(liba)
libaksorba = liba
libaksorba.sort()
print(libaksorba)
libakvisszafele = libaksorba
libakvisszafele.reverse()
print(libakvisszafele)