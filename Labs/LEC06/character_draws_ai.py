# LEC06 점진적 개발 실습 (AI 활용)
# 캐릭터가 원운동 → 사각 운동 → 삼각 운동을 차례로 한 바퀴씩 이동하고, 이를 무한 반복한다.
from pico2d import *
import math

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600

CENTER_X, CENTER_Y = 400, 300   # 원운동 중심
RADIUS = 200                    # 원운동 반지름

LEFT, RIGHT = 50, 750           # 사각 운동 x 범위
BOTTOM, TOP = 50, 550           # 사각 운동 y 범위
RECT_STEP = 5                   # 사각 운동 이동 간격

A = (100, 100)                  # 삼각 운동 꼭짓점
B = (700, 100)
C = (400, 500)
LINE_STEPS = 100                # 선분 하나를 나누는 구간 수


def draw_boy(x, y):
    # 지정한 좌표에 캐릭터를 그리고 화면을 갱신한다 (지우기 → 그리기 → 갱신 → 대기)
    get_events()
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(0.01)


def move_circle():
    # 중심 (400, 300), 반지름 200인 원을 반시계 방향으로 한 바퀴 돈다
    print('circle')
    for degree in range(0, 360):
        theta = math.radians(degree)
        x = CENTER_X + RADIUS * math.cos(theta)
        y = CENTER_Y + RADIUS * math.sin(theta)
        draw_boy(x, y)


def move_top():
    # 상단: y 고정, x 증가
    print('top')
    for x in range(LEFT, RIGHT + 1, RECT_STEP):
        draw_boy(x, TOP)


def move_right():
    # 오른쪽: x 고정, y 감소
    print('right')
    for y in range(TOP, BOTTOM - 1, -RECT_STEP):
        draw_boy(RIGHT, y)


def move_bottom():
    # 하단: y 고정, x 감소
    print('bottom')
    for x in range(RIGHT, LEFT - 1, -RECT_STEP):
        draw_boy(x, BOTTOM)


def move_left():
    # 왼쪽: x 고정, y 증가
    print('left')
    for y in range(BOTTOM, TOP + 1, RECT_STEP):
        draw_boy(LEFT, y)


def move_rectangle():
    # 상단 → 오른쪽 → 하단 → 왼쪽 순서로 사각형을 시계 방향으로 한 바퀴 돈다
    print('rectangle')
    move_top()
    move_right()
    move_bottom()
    move_left()


def move_line(p0, p1):
    # 진행 비율 t를 0에서 1까지 늘리며 p0에서 p1까지 직선으로 이동한다
    x0, y0 = p0
    x1, y1 = p1
    for i in range(LINE_STEPS + 1):
        t = i / LINE_STEPS
        x = (1 - t) * x0 + t * x1
        y = (1 - t) * y0 + t * y1
        draw_boy(x, y)


def move_a_to_b():
    print('a to b')
    move_line(A, B)


def move_b_to_c():
    print('b to c')
    move_line(B, C)


def move_c_to_a():
    print('c to a')
    move_line(C, A)


def move_triangle():
    # A → B → C → A 순서로 삼각형을 한 바퀴 돈다
    print('triangle')
    move_a_to_b()
    move_b_to_c()
    move_c_to_a()


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
boy = load_image('character.png')

while True:
    move_circle()
    move_rectangle()
    move_triangle()

close_canvas()
