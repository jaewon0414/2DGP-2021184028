import math

from pico2d import *

WIDTH, HEIGHT = 800, 600

# 프레임: (left, bottom, width, height, ax, ay)
#   left, bottom, width, height : 시트에서 잘라낼 영역 - pico2d 이미지 좌표 (왼쪽 아래가 원점)
#   ax, ay : 프레임 왼쪽 아래 모서리에서 캐릭터 발 밑(바닥 기준점)까지의 거리
#            프레임마다 크기가 달라도 이 점을 화면의 같은 위치에 맞추면 캐릭터가 흔들리지 않음
IDLE = (
    (4, 209, 19, 44, 11, 1),
    (27, 209, 19, 43, 11, 1),
    (50, 209, 19, 43, 11, 1),
    (73, 209, 19, 44, 11, 1),
)

WALK = (
    (4, 161, 20, 44, 11, 1),
    (28, 161, 22, 44, 11, 1),
    (54, 161, 26, 43, 13, 1),
    (84, 161, 20, 44, 11, 1),
    (108, 161, 20, 44, 11, 1),
    (132, 161, 22, 43, 11, 1),
)

RUN = (
    (4, 113, 23, 44, 11, 0),
    (31, 113, 28, 43, 14, 1),
    (63, 113, 36, 40, 17, 1),
    (103, 113, 33, 40, 17, 1),
    (140, 113, 23, 44, 11, 0),
    (167, 113, 26, 43, 12, 1),
    (197, 113, 32, 40, 15, 1),
    (233, 113, 29, 40, 15, 1),
)

JUMP = (
    (4, 65, 21, 40, 8, 1),
    (29, 65, 22, 44, 9, -2),
    (55, 65, 23, 42, 9, -11),
    (82, 65, 26, 41, 11, -15),
    (112, 65, 27, 44, 12, -9),
    (143, 65, 25, 40, 7, 1),
    (172, 65, 19, 44, 9, 1),
)

ATTACK = (
    (4, 4, 33, 43, 13, 1),
    (41, 4, 38, 49, 26, 1),
    (83, 4, 52, 57, 18, 1),
    (139, 4, 52, 51, 18, 1),
    (195, 4, 47, 40, 18, 1),
    (246, 4, 36, 43, 13, 1),
)

# Sprite -> Action들의 tuple -> Frame들의 tuple
SPRITE = (IDLE, WALK, RUN, JUMP, ATTACK)
ACTION_NAMES = ('Idle', 'Walk', 'Run', 'Jump', 'Attack')

# action별 프레임 시간(초) - 동작 성격에 맞게 자연스러운 속도로 조절
#   Idle: 느린 호흡 / Walk: 보통 걸음 / Run: 빠른 발놀림 / Jump: 체공감 / Attack: 빠르고 날카롭게
FRAME_TIME = (0.2, 0.12, 0.07, 0.1, 0.08)

# 서 있는 캐릭터의 키가 화면 높이의 절반 이상이 되도록 정수 배율 계산
CHARACTER_HEIGHT = max(frame[3] for frame in IDLE)
SCALE = math.ceil((HEIGHT / 2) / CHARACTER_HEIGHT)

# 화면에서 캐릭터 발 밑이 놓일 위치 - 서 있는 캐릭터가 화면 중앙에 오도록 설정
GROUND_X = WIDTH // 2
GROUND_Y = HEIGHT // 2 - CHARACTER_HEIGHT * SCALE // 2


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(WIDTH, HEIGHT)
hide_lattice()  # 배경 격자 숨기기

grass = load_image('grass.png')
hero = load_image('hero_sheet.png')

running = True
action = 0
frame = 0
loop = 0

while running:
    handle_events()

    if frame == 0 and loop == 0:  # 새 action 시작
        print(f'[{ACTION_NAMES[action]}] {len(SPRITE[action])}프레임 x 5회 재생')

    left, bottom, width, height, ax, ay = SPRITE[action][frame]

    # 기준점(ax, ay)이 (GROUND_X, GROUND_Y)에 오도록 프레임 중심 위치 계산
    x = GROUND_X + (width / 2 - ax) * SCALE
    y = GROUND_Y + (height / 2 - ay) * SCALE

    clear_canvas()
    grass.draw(WIDTH // 2, GROUND_Y - grass.h // 2 + 10)  # 발 밑에 잔디 바닥
    hero.clip_draw(left, bottom, width, height, x, y, width * SCALE, height * SCALE)
    update_canvas()

    frame_time = FRAME_TIME[action]  # 방금 그린 프레임의 action 기준으로 표시 시간 결정

    # action마다 프레임 수가 다르므로 현재 action의 프레임 수로 순환
    frame = (frame + 1) % len(SPRITE[action])

    # 한 바퀴를 다 돌면 반복 횟수 증가, 5회 반복하면 다음 action으로 (마지막 다음은 처음으로)
    if frame == 0:
        loop += 1
        if loop == 5:
            delay(1.0)  # 마지막 프레임이 화면에 남은 채로 1초 정지
            loop = 0
            action = (action + 1) % len(SPRITE)

    delay(frame_time)

close_canvas()
