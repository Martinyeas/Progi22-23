import turtle
import random
ablak = turtle.Screen()
Nori = turtle.Turtle()
randtablazat = ["e","h","j","b"]
ablak.bgcolor("lightgreen")
ablak.title("Hello 10e!")

i=0
while i<300:
    i+=1
    randtablarand = random.choice(randtablazat)
    if randtablarand == "e":
        Nori.forward(random.randint(0,100))
    elif randtablarand == "h":
        Nori.back(random.randint(0,100))
    elif randtablarand == "j":
        Nori.right(random.randint(0,100))
    elif randtablarand == "b":
        Nori.left(random.randint(0,100))

ablak.mainloop()