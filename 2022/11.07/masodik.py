t = [2,5,6,9,10,12,4]
n = len(t)
ker = 5
i = 0
wr = open("11.07\e.txt","w")
while i<n and t[i] != ker:
    i+=1
if i<n:
    print("Van ilyen ",ker)
    wr.write(f"Van ilyen {ker}")
else:
    print("Nincs ilyen ",ker)

while t[i]!=ker:
    i=i+1
print("Ezen a helyen található ",i+1)

print("lineáris keresés")

while i<n and t[i] != ker:
    i=i+1
    if i<n:
        print(f"van {ker} elem a listában")
        print(f"Helye {i+1}")
    else:
        print(f"nincs {ker} elem a listában")

maxElem =t[0]
for elem in t:
    if elem > maxElem:
        maxElem = elem
print(maxElem)

minElem =t[0]
for elem in t:
    if elem < minElem:
        minElem = elem
print(minElem)

print(f"Egyszerű számtani átlag : {(minElem)}")