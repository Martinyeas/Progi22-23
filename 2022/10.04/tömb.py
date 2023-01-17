t = [6,4,2,1,5,8,5]
t1 = ["d","e","f","g","h","i"]

osszeg = 0
n = len(t)
ker = 5
count = 0
szorzat = 1
konkat = " "
for num in t:
    osszeg = osszeg + num
    szorzat = szorzat * num
for num in t1:
    konkat = konkat + num
for num in t:
    if num > 5:
        count = count+1
i = 0
while i < n and t[i] != ker:
    i = i+1
if i < n:
    print("Van ilyen:",ker)
else:
    print("")
while t[i] != ker:
    i +=1
print("Hányadik helyen van:",i+1)

print("Összeg:",osszeg)
print("Szorzat:",szorzat)
print("Konkat:",konkat)
print("5-nél nagyobb számok:",count)