import vpython as vp
# from Cube_Piece import Cube_Piece
from Initialize_Cube import Color_Cube,Mirror_Cube
from Commands import *
from time import sleep

Cube = Color_Cube()
sleep(5)
i = 0

fps = 2
for i in range(1):
    vp.rate(fps)
    R(Cube)
    L_(Cube)
    F(Cube)
    B_(Cube)
    U(Cube)
    D_(Cube)
    R(Cube)
    L_(Cube)
    i += 1

sleep(10)