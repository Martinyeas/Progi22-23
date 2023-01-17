import pygame
import opensimplex
import random
import time

pygame.init()

m,sz = 1920,1080
ablak = pygame.display.set_mode((m,sz))
ablak.fill((0,0,0))
freq = (1/64)
res = 10
move = 0
szarazfoldi_biomok = ["erdo","alfold"]

while True:
    ablak.fill((0,0,0))
    for x in range(1,m,res):
        for y in range(1,sz,res):
            nval = opensimplex.noise2(x*freq+move,y*freq)
            if nval < 0 and nval > -1:
                if nval < -0.5:
                    pygame.draw.rect(ablak,(0,0,255),(x,y,res,res))
                else:
                    pygame.draw.rect(ablak,(40,40,255),(x,y,res,res))
            elif nval >0.25 and nval < 0.74:
                pygame.draw.rect(ablak,(0,255,0),(x,y,res,res))
            elif nval < -1 or nval > 1:
                pygame.draw.rect(ablak,(0,255,0),(x,y,res,res))
            elif nval >0 and nval <0.25:
                pygame.draw.rect(ablak,(255,255,0),(x,y,res,res))
            elif nval > 0.74:
                pygame.draw.rect(ablak,(255,255,255),(x,y,res,res))

    pygame.display.flip()
    time.sleep(0.01)
    opensimplex.seed(random.randint(256,49456))
   # move+=freq*50