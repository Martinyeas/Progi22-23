import pygame
import random

pygame.init()
w,h = 800,400
scr = pygame.display.set_mode((w,h))

aimw,aimh = 20,20
x,y = random.randint(0,w-aimw),random.randint(0,h-aimh)

cheat = True

timer = 60
pontok_szam = 0
fnt = pygame.font.SysFont("timesnewroman",65)
pontok = fnt.render("0",False,(255,255,255),(0,0,0))
#pontokrct = pontok.get_rect()

pontrect = pygame.Rect(x,y,aimw,aimh)
pontszin = (255,0,0)

running = True
while running:
    scr.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                if cheat:
                    cheat = False
                else:
                    cheat = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] > x-aimw and pygame.mouse.get_pos()[0] < x+aimw and pygame.mouse.get_pos()[1] > y-aimh and pygame.mouse.get_pos()[1] < y+aimh:
                x,y = random.randint(0,w-aimw),random.randint(0,h-aimh)
                pontok_szam += 1
                pontrect = pygame.Rect(x,y,aimw,aimh)
                pontok = fnt.render(str(pontok_szam),False,(255,255,255),(0,0,0))
                print(pontok_szam)
                
            else:
                pontok_szam -= 1
                pontok = fnt.render(str(pontok_szam),False,(255,255,255),(0,0,0))
                print(pontok_szam)
    if cheat:
        pygame.mouse.set_pos([pontrect.x+pontrect.width/2,pontrect.y+pontrect.height/2])
    scr.blit(pontok,(w/2,0))
    pygame.draw.rect(scr,pontszin,pontrect)
    pygame.display.flip()