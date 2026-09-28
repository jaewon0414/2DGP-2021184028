from pico2d import *
import math

open_canvas(800,600)

character = load_image('character.png')

def move_circle():
    print('circle')
    for degree in range(0,360,90):
        theta = math.radians(degree)
        x=400+200*math.cos(theta)
        y=300+200*math.sin(theta)
        print(degree,round(x),round(y))
    pass

def move_rectangle():
    print('rectangle')
    pass

def move_triangle():
    print('triangle')
    pass

clear_canvas()
character.draw(400,300)
update_canvas()

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    break

delay(2)
close_canvas()