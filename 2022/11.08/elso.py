t = [2,5,6,9,10,12,4]
wr = open("11.08\e.txt","w")
b=[]
c=[]
d=[]
e=[]
f=[]

def dupla(szam):
    return szam*2

for elem in t:
    b.append(dupla(elem))
    if elem%2 == 0:
        c.append(elem)
    elif elem < 5:
        d.append(elem)
    elif elem%2 != 0:
        e.append(elem)
    elif elem > 5:
        f.append(elem)
print(b)
print(c)
print(d)
print(e)
maxElem =t[0]
for elem in t:
    if elem > maxElem:
        maxElem = elem
wr.write(f"{str(maxElem)} \n")

minElem =t[0]
for elem in t:
    if elem < minElem:
        minElem = elem
wr.write(f"{str(minElem)} \n")

wr.close()

#buborék rendezés

n = len(t)
for i in range(n-1,0,-1):
    for j in range(0,i):
        if [t[i]>t[i+1]]:
            tmp = t[j+1]
            t[j+1]=t[j]
            t[j] = tmp

print(t)