from xmlrpc.client import TRANSPORT_ERROR
import pygame
import opensimplex
import random
import time

pygame.init()

m,sz = 500,500
ablak = pygame.display.set_mode((m,sz))
ablak.fill((0,0,0))
res = 10

actv_x = []
actv_y = []

def keres(x,y):
    for i in actv_x:
        if actv_x -1 == x and actv_y == y:
            return True
        elif actv_x +1 == x and actv_y == y:
            return True
        elif actv_x +1 == x and actv_y+1 == y:
            return True
        elif actv_x +1 == x and actv_y-1 == y:
            return True
        elif actv_x -1 == x and actv_y+1 == y:
            return True
        elif actv_x -1 == x and actv_y-1 == y:
            return True
        elif actv_x == x and actv_y+1 == y:
            return True
        elif actv_x == x and actv_y-1 == y:
            return True
        else:
            return False

while True:
    ablak.fill((0,0,0))
    x = random.randint(1,m-1)
    y = random.randint(1,sz-1)
    pygame.draw.rect(ablak,(120,120,120),(x,y,res,res))
    actv_x.append(x)
    actv_y.append(y)
    
    if not keres():
        actv_x.remove(x)
        actv_y.remove(y)
    
    pygame.display.flip()
    time.sleep(1)