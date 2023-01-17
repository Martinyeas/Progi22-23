import pygame
import random
import math
import time

pygame.init()

w,h = 800,800
scr = pygame.display.set_mode((w,h))
r = 50
sz = 0
seb = 300
szam = 0
deb = True
sz1 = (255,255,0)
sz2 = (0,255,0)
off = 30
sinoff1 = random.randint(1,3)*15
sinoff2 = random.randint(3,5)*12
sinoff3 = random.randint(5,7)*20
sinoff4 = random.randint(7,9)*20
while True:
    scr.fill((0,0,0))
    sz+=1
    
    if szam == 0:
        if math.sin(sz/seb) > 0:
            pygame.draw.rect(scr,sz1,((w/2-r/2)-off,h/2+math.cos(sz/seb+sinoff1)*h/2-r/2,r,r),r,10)
            pygame.draw.rect(scr,sz1,((w/2-r/2)+off,h/2+math.sin(sz/seb+sinoff2)*h/2-r/2,r,r),r,10)

            pygame.draw.rect(scr,sz1,(w/2+math.cos(sz/seb+sinoff3)*w/2-r/2,(h/2-r/2)-off,r,r),r,10)
            pygame.draw.rect(scr,sz1,(w/2+math.sin(sz/seb+sinoff4)*w/2-r/2,(h/2-r/2)+off,r,r),r,10)
        else:
            pygame.draw.rect(scr,sz1,((w/2-r/2)-off,h/2+math.cos(sz/seb+sinoff1)*h/2-r/2,r,r),r,10)
            pygame.draw.rect(scr,sz1,((w/2-r/2)+off,h/2+math.sin(sz/seb+sinoff2)*h/2-r/2,r,r),r,10)

            pygame.draw.rect(scr,sz1,(w/2+math.cos(sz/seb+sinoff3)*w/2-r/2,(h/2-r/2)-off,r,r),r,10)
            pygame.draw.rect(scr,sz1,(w/2+math.sin(sz/seb+sinoff4)*w/2-r/2,(h/2-r/2)+off,r,r),r,10)
    else:
        if math.sin(sz/seb) > 0:
            pygame.draw.rect(scr,sz1,(h/2+math.sin(sz/seb)*h/2-r/2,h/2-r/2,r,r))
        else:
            pygame.draw.rect(scr,sz2,(h/2+math.sin(sz/seb)*h/2-r/2,h/2-r/2,r,r))
            

    pygame.display.update()
    time.sleep(0.0001)