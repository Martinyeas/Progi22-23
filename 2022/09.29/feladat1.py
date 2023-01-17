print("For ciklus.")
for i in range(1,101):
    print(i)
for i in range(101):
    print(i)
for i in range(1,101,2):
    print(i)
for i in range(100,1,-1):
    print(i)
ossz = 0
for i in range(1,101):
    ossz = ossz + i

print(ossz)
ossz = 0
szaml = 0
while szaml <100:
    szaml +=1
    ossz = szaml+ossz

print(ossz)

string = input("Kérem adja meg a nevét")
print(string)
print(len(string[0]))
