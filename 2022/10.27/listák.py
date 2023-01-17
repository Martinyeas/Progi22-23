def feladat_1():
    honap = ["január","február","március"]
    print(honap[2])
    print(honap)
    nev = []
    nev.append("Glázser Bozsó")
    print(nev[0])
    nev[0] = "Nyomasek Bobó"
    print(nev[0])
    szuletes = [0]*40
    szuletes[29] = 1
    print(szuletes[29])
    print(honap[szuletes[29]])

def feladat_2():
    tippek = [3,12,1,8,5,8,1,2,1,4]
    print(tippek.index(2)+1)
    masolat = tippek.copy()
    del tippek[3:5]
    print(tippek)
    tippek.sort()
    print(tippek)
    tippek.reverse()
    print(masolat)
    hivatkozas = tippek
    tippek.remove(12)
    print(tippek)
    print(hivatkozas)
feladat_1()
feladat_2()