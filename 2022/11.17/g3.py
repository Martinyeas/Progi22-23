import math
import time
import opensimplex
import pygame
import random

pygame.init()

w,h = 500,500
sc = pygame.display.set_mode((w,h))
sc.fill((0,0,0))
res = 10
feher = (255,255,255)
maxnum = 8**69
opensimplex.seed = random.randint(1024,maxnum)
mult = 100

for x in range(0,w,res):
    for y in range(0,h,res):
        no = opensimplex.noise2(x,(h/2)*res)*mult
        pygame.draw.rect(sc,feher,(x,h/2+no,res,res))

while True:
    pygame.display.update()