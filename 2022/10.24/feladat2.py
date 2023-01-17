def alahuzas():
    for i in range(10):
        print(i)
print("ez egy fontos figyelmeztetés!")
alahuzas()
print("Minden sora nagyon fontos!")
alahuzas()

def pluszketto(szam):
    print(szam + 2)
print("5+2=",pluszketto(5))


t = [2,5,6,9,10,12,4]
maxElem = t[0]
for elem in t:
    if elem > maxElem:
        maxElem = elem
print(maxElem)

minElem = t[0]
for elem in t:
    if elem < minElem:
        minElem = elem
print(minElem)