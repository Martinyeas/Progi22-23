class híres_auto:
    def __init__(self, marka, henger_terfogat, nemzetiseg):
        self.marka = marka
        self.henger_terfogat = henger_terfogat
        self.nemzetiseg = nemzetiseg

    def nemzetiség(self):
        if str.lower(self.nemzetiseg) == "j":
            return "Japán"
        elif str.lower(self.nemzetiseg) == "n":
            return "Német"
