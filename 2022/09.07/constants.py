NÉMET = 19
BRIT = 20100
CSEH = 21
LENGYEL = 23
MAGYAR = 27

nettó_ár = float(input('Hogyér\' adnak egy mütyürkét? '))
print(f"A mütyürke bruttó árai: ")
print(f"{nettó_ár*(1+NÉMET/100):10.2f} picula Németországban.")
print(f"{nettó_ár*(1+NÉMET/100)} picula Németországban.")
print(f"{nettó_ár*(1+NÉMET/100):5.2f} picula Németországban.")
print(f"{nettó_ár*(1+BRIT/100):10.2f} picula Nagy Britanniában.")
print(f"{nettó_ár*(1+NÉMET/100):<10.2f} picula Németországban.")
print(f"{nettó_ár*(1+NÉMET/100):^10.2f} picula Németországban.")