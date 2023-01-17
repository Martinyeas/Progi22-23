from errno import WSAEHOSTDOWN


kacatok = ["csat","gombolyag","vonatjegy"]
print(kacatok)
kacatok.append("kulcskarika")
print(kacatok)
print(', '.join(kacatok))

kacat = "bármi"
while str.lower(kacat) != "elfogyott":
    kacat = input("adjon meg egy kacatot ")
    if str.lower(kacat) != "elfogyott":
        kacatok.append(kacat)
print(kacatok)