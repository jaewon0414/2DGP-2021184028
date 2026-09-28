from pico2d import *
import math
CENTER_X=400
CENTER_Y=300
RADIUS=200

open_canvas(800,600)

character = load_image('character.png')

def move_circle():
    print('circle')
    for degree in range(360):
        theta = math.radians(degree)
        x=CENTER_X+RADIUS*math.cos(theta)
        y=CENTER_Y+RADIUS*math.sin(theta)

        clear_canvas()
        character.draw(x,y)
        update_canvas()
        delay(0.01)
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