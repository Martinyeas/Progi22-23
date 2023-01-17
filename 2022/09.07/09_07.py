a=int(input("kérek egy számot "))
b=int(input("kérek még egy számot "))
c=a+b

print(a)
print(b)
print(a+b)
print(c)

print(f'Az {a} és {b} összege {c}-vel egyenlő')

if a>b:
    print(f"{a} nagyobb mint {b}")
elif b>a:
    print(f"{b} nagyobb mint {a}")
elif a==b:
    print(f"{a} egyenlő {b}-vel")
    
if a%2==0:
    print("páros")

#------------------------------------------
