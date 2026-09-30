import math

from pico2d import *

WIDTH, HEIGHT = 800, 600

# 프레임: (left, bottom, width, height) - pico2d 이미지 좌표 (왼쪽 아래가 원점)
IDLE = (
    (4, 209, 19, 44),
    (27, 209, 19, 43),
    (50, 209, 19, 43),
    (73, 209, 19, 44),
)

WALK = (
    (4, 161, 20, 44),
    (28, 161, 22, 44),
    (54, 161, 26, 43),
    (84, 161, 20, 44),
    (108, 161, 20, 44),
    (132, 161, 22, 43),
)

RUN = (
    (4, 113, 23, 44),
    (31, 113, 28, 43),
    (63, 113, 36, 40),
    (103, 113, 33, 40),
    (140, 113, 23, 44),
    (167, 113, 26, 43),
    (197, 113, 32, 40),
    (233, 113, 29, 40),
)

JUMP = (
    (4, 65, 21, 40),
    (29, 65, 22, 44),
    (55, 65, 23, 42),
    (82, 65, 26, 41),
    (112, 65, 27, 44),
    (143, 65, 25, 40),
    (172, 65, 19, 44),
)

# Sprite -> Action들의 tuple -> Frame들의 tuple
SPRITE = (IDLE, WALK, RUN, JUMP)

# 서 있는 캐릭터의 키가 화면 높이의 절반 이상이 되도록 정수 배율 계산
CHARACTER_HEIGHT = max(frame[3] for frame in IDLE)
SCALE = math.ceil((HEIGHT / 2) / CHARACTER_HEIGHT)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(WIDTH, HEIGHT)

hero = load_image('hero_sheet.png')

running = True
action = 0
frame = 0

while running:
    handle_events()

    left, bottom, width, height = SPRITE[action][frame]

    clear_canvas()
    hero.clip_draw(left, bottom, width, height,
                   WIDTH // 2, HEIGHT // 2, width * SCALE, height * SCALE)
    update_canvas()

    frame = (frame + 1) % 4
    delay(0.1)

close_canvas()
