class EGYETEM():
    def __init__(self,egyetemnév,város,nemzetiség):
        self.nev = egyetemnév
        self.varos = város
        self.nemzetiseg = nemzetiség
    def nemzetiseg_valto(self):
        if str.lower(self.nemzetiseg) == "n":
            return "Universität"
        elif str.lower(self.nemzetiseg) == "a":
            return "University"