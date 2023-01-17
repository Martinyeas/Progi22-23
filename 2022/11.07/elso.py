import math

wr = open('./11.07/osz.txt','w')

szam = 0
while szam < 100:
    wr.write(f"{str(math.sin(szam))}\n")
    szam+=1

