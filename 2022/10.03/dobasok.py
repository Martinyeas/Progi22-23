import random
szamlalo = 0
t = []
while szamlalo <= 10**6:
    szamlalo+=1
    dobas = random.choice(["1","2","3","4","5","6"])
    t.append(dobas)
print(t)
print(t.count("1"))
