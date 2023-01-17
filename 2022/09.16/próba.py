import math
import random

obj_vel = 0
obj_mass =random.randint(1,10)
obj_h = random.randint(1,10)

h_min = 0

def grav():
    if obj_h > h_min:
        obj_h -= obj_vel
    elif obj_h < h_min:
        obj_h = h_min
    else:
        obj_h = h_min
        obj_vel = 0

while obj_h>h_min:

    print(obj_h)