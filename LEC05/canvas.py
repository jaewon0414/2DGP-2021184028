from pico2d import *
import math

open_canvas(800, 600)

grass = load_image('grass.png')
character = load_image('character.png')

cx, cy = 400, 300   # 원운동 기준 중심 좌표
radius = 100          # 반지름
angle = 0             # 각도, 반복문 안에서 계속 바뀜
angle_speed = 0.1    # 한 프레임마다 각도가 증가하는 양

grass.draw(400, 30)

while angle < 20:   # 일단 각도가 20(라디안)이 될 때까지만 반복
    clear_canvas()

    x = cx + radius * math.cos(angle)
    y = cy + radius * math.sin(angle)
    character.draw(x, y)

    update_canvas()

    angle += angle_speed
    delay(0.01)

close_canvas()