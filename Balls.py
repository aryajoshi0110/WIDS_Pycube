from vpython import *
from time import sleep

# Ball in a room
Ball_radius = 0.75
wall_Thickness = 0.5
Room_Height = 20
Room_Width = 50
Room_Depth = 5
x_blue , y_blue , z_blue = 0 , 0 , 0
x_red , y_red , z_red = 0 , 0 , 0
dx = 1
dy = 1

Ceiling = box(pos=vector(0,Room_Height/2,0),size=vector(Room_Width,wall_Thickness,Room_Depth),color=color.white)
Floor = box(pos=vector(0,-Room_Height/2,0),size=vector(Room_Width,wall_Thickness,Room_Depth),color=color.white)
Left_Wall = box(pos=vector(-Room_Width/2,0,0),size=vector(wall_Thickness,Room_Height,Room_Depth),color=color.white)
Right_Wall = box(pos=vector(Room_Width/2,0,0),size=vector(wall_Thickness,Room_Height,Room_Depth),color=color.white)
Back_Wall = box(pos=vector(0,0,-Room_Depth/2),size=vector(Room_Width,Room_Height,wall_Thickness),color=color.white)
Blue_Ball = sphere(pos=vector(x_blue,y_blue,z_blue),radius=Ball_radius,color=color.blue)
Red_Ball = sphere(pos=vector(x_red,y_red,z_red),radius=Ball_radius,color=color.red)

while True:
    rate(10)
    if abs(x_blue) >= (Room_Width/2 - wall_Thickness/2 - Ball_radius):
        dx *= -1
    if abs(y_red) >= (Room_Height/2 - wall_Thickness - Ball_radius):
        dy *= -1
    x_blue += dx
    y_red += dy
    Blue_Ball.pos = vector(x_blue,y_blue,z_blue)
    Red_Ball.pos = vector(x_red,y_red,z_red)
    pass