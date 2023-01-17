import pygame
import random
import os

pygame.init()

w,h = 800,450
scr = pygame.display.set_mode((w,h))
bg = (0,0,0)
ido = 4
scr.fill(bg)
kockax,kockay = 80,45
x,y = random.randint(0+kockax,w-kockax),random.randint(0+kockay,h-kockay)
velx,vely = -2,2
l = False
r = False
u = False
d = False
kockacol = (255,255,255)
running = True
keydown = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not keydown:
                keydown = True
        if event.type == pygame.MOUSEBUTTONUP:
            if keydown:
                keydown = False
    scr.fill(bg)
    pygame.time.delay(ido)
    if x>w-kockax or x<0:
        velx=-velx
        kockacol = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
    elif y>h-kockay or y<0:
        vely=-vely
        kockacol = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
    if not keydown:
        x = x+velx
        y = y+vely
    else:
        x,y = pygame.mouse.get_pos()
        
    pygame.draw.rect(scr,kockacol,(x,y,kockax,kockay))

    pygame.display.flip()
    