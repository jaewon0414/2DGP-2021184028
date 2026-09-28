from pico2d import *
import math
CENTER_X=400
CENTER_Y=300
RADIUS=200

open_canvas(800,600)

character = load_image('character.png')

def draw_boy(x,y):
    get_events()
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
    for x in range(50,751,5):
        draw_boy(x,550)

def move_right():
    print('right')
    for y in range(550,49,-5):
        draw_boy(750,y)

def move_bottom():
    print('bottom')
    for x in range(750,49,-5):
        draw_boy(x,50)

def move_left():
    print('left')
    for y in range(50,551,5):
        draw_boy(50,y)

def move_rectangle():
    print('rectangle')
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass

def move_a_to_b():
    print('a to b')
    x0, y0=100,100
    x1, y1=700,100
    n=100
    for step in range(n+1):
        t=step/n
        x=x0+(x1-x0)*t
        y=y0+(y1-y0)*t
        draw_boy(x,y)

def move_b_to_c():
    print('b to c')

def move_c_to_a():
    print('c to a')

def move_triangle():
    print('triangle')
    move_a_to_b()
    move_b_to_c()
    move_c_to_a()
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