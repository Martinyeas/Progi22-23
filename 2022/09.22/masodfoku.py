from asyncio import constants
import math
import random

A = 2
b = random.randint(0,5)
c = int(input("Adjon meg egy számot: "))

print(A+b+c)
print(A*b*c)

lista = [A,b,c]

while A != 0:
    A = int(input("Adjon meg egy számot 0-5ig "))

print(f"Az A = {A}")
A=10
d = A*math.pi+b*c
print(d)

biig = 0
for x in range(0,101):
    for y in range(0,101):
        if x+y > biig:
            biig = x+y
print(biig)