import math
import random

m = int(input("Adja meg a henger magasságát: "))
r = int(input("Adja meg a henger sugarát: "))

#m = random.randint(2,10)
#r =random.randint(2,10)


Ta = math.pow(r,2)*math.pi
Tp = 2*math.pi*r*m
terfogat = Ta*m
felszin = 2* Ta+Tp

print(f'{terfogat:10.2f}',"cm^3")
print(f'{felszin:10.2f}',"cm^2")