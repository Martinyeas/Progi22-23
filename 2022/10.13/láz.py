holista = []
nevlista = []

for i in range(1,4):
    nevlista.append(input("Mi az ön neve? "))
    holista.append(float(input("Hány fokos a testhőmérséklete? ")))


felett37 = 0
for i in range(0,len(holista)):
    if holista[i] > 37.9:
        print(nevlista[i],"Láz")
    elif holista[i] > 36.9 and holista[i] < 38.0:
        print(nevlista[i],"Hőemelkedés")
    else:
        print(nevlista[i],"Normális")
    if holista[i] > 37:
        felett37 +=1
print(felett37,"van 37 fok felett.")