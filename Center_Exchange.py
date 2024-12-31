import vpython as vp
from Initialize_Cube import Color_Cube,Mirror_Cube
from Commands import *
from time import sleep

Cube = Color_Cube()
sleep(5)
i = 0

for move in [R,L_,F,B_,U,D_,R,L_]:
    move(Cube)

sleep(10)
