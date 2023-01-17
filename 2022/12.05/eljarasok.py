def border(n,s):
    print()
    for i in range(n):
        print(s,sep="",end="")
    print("\n")

border(80,"*")
print("1. feladat")
border(10,"-")
print("3. feladat")
border(80,"*")
print("4. feladat")

def proc():
    a = 5
    print(b)
    print(c)

b = 0
c = 4
proc()

def proc(x):
    x +=1
    print(x)
proc(3)
a = 10
proc(a)
print(a)

def pn(num):
    end = int(num/2)
    s = 1
    for i in range(2,end+1):
        if num % i == 0:
            s += 1
    if s == num:
        print("Tökéletes szám")
    else:
        print("Nem Tökéletes")

for i in range(2,1001):
    print(i,end=" ")
    pn(i)
ob = int(input("Kérek vizsgálandó számot: "))
pn(ob)