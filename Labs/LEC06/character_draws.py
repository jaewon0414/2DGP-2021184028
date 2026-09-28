#LEF06 점진적 개발 실습
from pico2d import *
import math
CENTER_X=400
CENTER_Y=300
RADIUS=200

open_canvas(800,600)

character = load_image('character.png')

def draw_boy(x,y):
    # 지정한 좌표에 캐릭터를 그리고 화면을 갱신한다
    get_events()
    clear_canvas()
    character.draw(x,y)
    update_canvas()
    delay(0.01)


def move_circle():
     # 중심 (400, 300), 반지름 200인 원을 반시계 방향으로 한 바퀴 돈다
    print('circle')
    for degree in range(360):
        theta = math.radians(degree)
        x=CENTER_X+RADIUS*math.cos(theta)
        y=CENTER_Y+RADIUS*math.sin(theta)

        draw_boy(x,y)

def move_top():
    # 상단 가로선을 따라 이동한다
    print('top')
    for x in range(50,751,5):
        draw_boy(x,550)

def move_right():
    # 우측 세로선을 따라 이동한다
    print('right')
    for y in range(550,49,-5):
        draw_boy(750,y)

def move_bottom():
    # 하단 가로선을 따라 이동한다   
    print('bottom')
    for x in range(750,49,-5):
        draw_boy(x,50)

def move_left():
    # 좌측 세로선을 따라 이동한다
    print('left')
    for y in range(50,551,5):
        draw_boy(50,y)

def move_rectangle():
    # 위 → 오른쪽 → 아래 → 왼쪽 순서로 사각형을 한 바퀴 돈다
    print('rectangle')
    move_top()
    move_right()
    move_bottom()
    move_left()

def move_line(x0,y0,x1,y1):
    # 시작점에서 끝점까지 직선으로 이동한다
    n=100
    for step in range(n+1):
        t=step/n
        x=x0+(x1-x0)*t
        y=y0+(y1-y0)*t
        draw_boy(x,y)

def move_a_to_b():
    print('a to b')
    move_line(100,100,700,100)

def move_b_to_c():
    print('b to c')
    move_line(700,100,400,500)

def move_c_to_a():
    print('c to a')
    move_line(400,500,100,100)

def move_triangle():
    # A(100,100) → B(700,100) → C(400,500) → A 순서로 삼각형을 한 바퀴 돈다
    print('triangle')
    move_a_to_b()
    move_b_to_c()
    move_c_to_a()
    pass


while True:
    move_circle()
    move_rectangle()
    move_triangle()

delay(2)
close_canvas()