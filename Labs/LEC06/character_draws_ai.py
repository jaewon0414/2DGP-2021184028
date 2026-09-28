# LEC06 점진적 개발 실습 (AI 활용)
# 캐릭터가 원운동 → 사각 운동 → 삼각 운동을 차례로 한 바퀴씩 이동하고, 이를 무한 반복한다.
from pico2d import *

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600


def draw_boy(x, y):
    # 지정한 좌표에 캐릭터를 그리고 화면을 갱신한다 (지우기 → 그리기 → 갱신 → 대기)
    get_events()
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(0.01)


def move_circle():
    print('circle')
    draw_boy(400, 300)
    delay(1)


def move_rectangle():
    print('rectangle')


def move_triangle():
    print('triangle')


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
boy = load_image('character.png')

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    break

close_canvas()
