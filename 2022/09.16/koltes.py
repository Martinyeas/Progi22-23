szerdakoltes = int(input("Mennyit költöttél szerdán? "))
keddkoltes = int(input("Mennyit költöttél kedden? "))

if szerdakoltes > keddkoltes:
    print(f"Szerdán költöttél többet, {szerdakoltes} Ft-ot")
elif szerdakoltes < keddkoltes:
    print(f"Kedden költöttél többet, {keddkoltes} Ft-ot")
else:
    print(f"Ugyanannyit költöttél, {keddkoltes} Ft-ot")
