roka = [2.5,4,6,7,2,3,4]

tomeg = 0
for i in roka:
    tomeg = tomeg + i
print(tomeg)

tobb = 0
for i in roka:
    if roka[i] > 3:
        tobb +=1
print(tobb)

van5kilos = False
for i in roka:
    if roka[i] ==5:
        van5kilos = True
if van5kilos:
    print("Van 5 kilós")