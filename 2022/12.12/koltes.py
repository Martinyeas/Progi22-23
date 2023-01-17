kedd = int(input("Hány forintot költöttél kedden? "))
szerda = int(input("Hány forintot költöttél szerdán? "))

if kedd > szerda:
    print(f"Kedden többet költöttél, {kedd}.")
elif szerda > kedd:
    print(f"Szerdán többet költöttél, {szerda}.")
else:
    print(f"{szerda} = {kedd}")