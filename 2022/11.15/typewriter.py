import time

szo = input("írjon be egy szót: ")
szam = 0
char = "aa"
while szam < 110000:
    szo = szo + chr(szam)
    szam+=1

def typewrite(szo):
    for i in szo:
        if i == " ":
            time.sleep(0.05)
            print(i,end="")
        else:
            print(i,end="")
            time.sleep(0.05)
typewrite(szo)
