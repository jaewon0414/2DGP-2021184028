from pico2d import *
import math
CENTER_X=400
CENTER_Y=300
RADIUS=200

open_canvas(800,600)

character = load_image('character.png')

def draw_boy(x,y):
    clear_canvas()
    character.draw(x,y)
    update_canvas()
    delay(0.01)


def move_circle():
    print('circle')
    for degree in range(360):
        theta = math.radians(degree)
        x=CENTER_X+RADIUS*math.cos(theta)
        y=CENTER_Y+RADIUS*math.sin(theta)

        draw_boy(x,y)
    pass

def move_top():
    print('top')

def move_right():
    print('right')

def move_bottom():
    print('bottom')

def move_left():
    print('left')

def move_rectangle():
    print('rectangle')
    move_top()
    move_right()
    move_bottom()
    move_left()
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