import math

a = int(input("o1 "))
b = int(input("o2 "))
c = int(input("o3 "))

K = a+b+c
s = K/2
T = s*math.sqrt(s-a)*(a-b)*(a-c)

print("Terület: ",T)
print("Kerület: ",K)

loopstable = 1

while True:
    loopstable += 1