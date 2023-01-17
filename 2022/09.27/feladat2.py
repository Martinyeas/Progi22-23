import random

f = []
for i in range(10):
    fs = random.choice(["f","í"])
    f.append(fs)
print("A feldobások:",", ".join(f))
fuf = 0
for i,fs in enumerate(f):
    if i > 0 and fs == "f" and f[i-1] == "f":
        fuf += 1
print("Ennyiszer volt fej után fej:",str(fuf))