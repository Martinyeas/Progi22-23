class Hires_katona:
    def __init__(self,nev,foglalkozas,nemzetiseg):
        self.nev = nev
        self.foglalkozas = foglalkozas
        self.nemzetiseg = nemzetiseg
    def elotag(self):
        if nemzetiseg == "n":
            return "Herr"
        else:
            return "Mister"

híres_katona = []
for _ in range(3):
    nev = input("Kérem adja meg a katona nevét! ")
    foglalkozas = input("Kérem adja meg a katona rangját! ")
    nemzetiseg = input("Kérem adja meg a katona nemzetiségét!(o,n) ")
    híres_katona1 = Hires_katona(nev,foglalkozas,nemzetiseg)
    híres_katona.append(híres_katona1)
for hkatona in híres_katona:
    print(f"{hkatona.elotag()} egy híres {hkatona.foglalkozas} aki egy {hkatona.nemzetiseg}")
    sz1 = hkatona.nemzetiseg
    sz2 = hkatona.nev

    print(f'capitalize {sz1.capitalize()}')
    print(f'capitalize {sz2.capitalize()}')

    print(f'endswith {sz1.endswith("a")}')
    print(f'endswith {sz2.endswith("a")}')

    print(f'find {sz1.find("o")}')
    print(f'find {sz2.find("l")}')

    print(f'isalnum {sz1.isalnum()}')
    print(f'isalnum {sz2.isalnum()}')

    print(f'isalpha {sz1.isalpha()}')
    print(f'isalpha {sz2.isalpha()}')

    print(f'islower {sz1.islower()}')
    print(f'islower {sz2.islower()}')

    print(f'join {sz1.join("w")}')
    print(f'join {sz2.join("w")}')



    print(f'lower {sz1.lower()}')
    print(f'lower {sz2.lower()}')

    print(f'lstrip {sz1.lstrip()}')
    print(f'lstrip {sz2.lstrip()}')

    print(f'replace {sz1.replace("o","ű")}')
    print(f'replace {sz2.replace("a","é")}')

    print(f'rfind {sz1.rfind("k")}')
    print(f'rfind {sz2.rfind("d")}')

    print(f'rstrip {sz1.rstrip()}')
    print(f'rstrip {sz2.rstrip()}')

    print(f'split {sz1.split()}')
    print(f'split {sz2.split()}')

    print(f'startswith {sz1.startswith("K")}')
    print(f'startswith {sz2.startswith("a")}')

    print(f'strip {sz1.strip()}')
    print(f'strip {sz2.strip()}')

    print(f'swapcase {sz1.swapcase()}')
    print(f'swapcase {sz2.swapcase()}')

    print(f'title {sz1.title()}')
    print(f'title {sz2.title()}')

    print(f'upper {sz1.upper()}')
    print(f'upper {sz2.upper()}')