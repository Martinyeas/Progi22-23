penz = 25000
kell_gep_mukodik = True
gep_ar = int(input("Mennyibe kerül? "))
gep_mukodik = True if str.lower(input("Működik? (i/n) ")) == "i" else False
gep_tipus = str.lower(input("Gép típusa? "))

if str.lower(gep_tipus) == str.lower("C64") or str.lower(gep_tipus) == str.lower("ZX") and gep_ar <= penz and gep_mukodik:
    print("Megvesszük.")
else:
    print("Nem vesszük meg.")