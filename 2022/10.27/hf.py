tantargyak = ['matek', 'töri', 'bio', 'kémia', 'info']

for tantargy in tantargyak:
	print(tantargy)

for i in range(10):
    print(i)

for i in range(5,9):
    print(i)

for i in range(3,21,6):
    print(i)


honapok = ['január', 'február','március', 'április', 'május', 'június'] 

index = 0
for honap in honapok:
    print(index, honap)
    index = index + 1


honapok = ['január', 'február','március', 'április', 'május', 'június']

for index in range(len(honapok)):
    print(index, honapok[index])


honapok = ['január', 'február','március', 'április', 'május', 'június']

for index, honap in enumerate(honapok):
    print(index, honap)


honapok = ['január', 'február','március', 'április', 'május', 'június']

for honap in honapok:
    honap = honap.upper()	


for index in range(len(honapok)):
    honapok[index] = honapok[index].upper()
