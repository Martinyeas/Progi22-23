class Hajo:
    def __init__(self,neve,kapitany,arboc,sebesseg,orszag):
        self.neve = neve
        self.kapitany = kapitany
        self.arboc = arboc
        self.sebesseg = sebesseg
        self.orszag = orszag
    def atalakit(self):
        return self.sebesseg * 1.852
    def arboc(self):
        return self.arboc/100
    def kapnev(self):
        return self.kapitany.capitalize()
    def nemzet(self):
        if str.lower(self.orszag) == "o":
            return "orosz"
        elif str.lower(self.orszag) == "a":
            return "amerikai"
    
hajok = []
for i in range(3):
    nev = input("Hajó nevét adja meg! ")
    kapinev = input("Kapitány nevét adja meg! ")
    hajoseb = int(input("Adja meg az egyik hajó sebességét! "))
    orsz = input("Adja meg a másik hajó országát! ")
    magassag = int(input("Adja meg az árbóc magasságot centiméterben: "))
    sello = Hajo(nev,kapinev,magassag,hajoseb,orsz)
    hajok.append(sello)
for hajo in hajok:
    print(f"{hajo.neve},{hajo.atalakit()},{hajo.arboc()},{hajo.kapnev()},{hajo.nemzet()}")