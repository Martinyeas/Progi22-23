import random

A = 3
b = random.randint(5,25)
c = int(input("Adjon egy számot "))

tablazat = [A,b,c]

if b%2 == 0:
    print("páros a b")
    
if c%2 != 0:
    print("páratlan a c")

print(A+b+c)
print(A*b*c)

if A*b*c > 500:
    print("Nagyobb mint 500")

if c%5 == 0:
    print("c öttel osztható")

tablazat.sort(reverse=False)
print(tablazat)
for i in tablazat:
    print(str(i)+", ",end="")