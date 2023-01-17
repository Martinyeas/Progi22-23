h = int(input("Milyen hosszú a kert? "))
sz = int(input("Milyen széles a kert? "))

halo = 50
kellene_halo = h*sz

if kellene_halo < halo:
    print(f"A kert bekerítéséhez {kellene_halo} méret drótháló kell.")
    print(f"Ki fog maradni {halo - kellene_halo} méter.")
elif kellene_halo > halo:
    print(f"A kert bekerítéséhez {kellene_halo} méret drótháló kell.")
    print(f"Venni kell még {kellene_halo-halo}")
elif kellene_halo == halo:
    print(f"A kert bekerítéséhez {kellene_halo} méret drótháló kell.")
    print(f"Pont elegendő háló van.")