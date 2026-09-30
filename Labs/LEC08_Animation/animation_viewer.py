from pico2d import *

WIDTH, HEIGHT = 800, 600

# 프레임: (left, bottom, width, height) - pico2d 이미지 좌표 (왼쪽 아래가 원점)
IDLE = (
    (4, 209, 19, 44),
    (27, 209, 19, 43),
    (50, 209, 19, 43),
    (73, 209, 19, 44),
)

# Sprite -> Action들의 tuple -> Frame들의 tuple
SPRITE = (IDLE,)

open_canvas(WIDTH, HEIGHT)

hero = load_image('hero_sheet.png')

action = 0
frame = 0

left, bottom, width, height = SPRITE[action][frame]

clear_canvas()
hero.clip_draw(left, bottom, width, height, WIDTH // 2, HEIGHT // 2)
update_canvas()

delay(1)

close_canvas()
