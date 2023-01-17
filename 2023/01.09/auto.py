from auto_alap import híres_auto

autok = []

for _ in range(3):
    marka = input("Kérem adja meg az autó márkáját: ")
    henger_terfogat = input("Kérem adja meg az autó henger térfogatát: ")
    nemzetiseg = input("Kérem adja meg az autó gyártó országát (J/N): ")

    autok.append(híres_auto(marka, henger_terfogat, nemzetiseg))

for auto in autok:
    print(f"{auto.nemzetiseg}: {auto.marka} ({auto.henger_terfogat} c2)")
