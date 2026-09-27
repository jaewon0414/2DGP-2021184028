from pico2d import *

open_canvas(800, 600)

grass = load_image('grass.png')
character = load_image('character.png')

x, y = 250, 200
speed = 5

grass.draw(400, 30)

# 1단계: 오른쪽으로 이동
while x < 500:
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    x += speed
    delay(0.01)

# 2단계: 위로 이동
while y < 400:
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    y += speed
    delay(0.01)

# 3단계: 왼쪽으로 이동
while x > 250:
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    x -= speed
    delay(0.01)

# 4단계: 아래로 이동
while y > 200:
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    y -= speed
    delay(0.01)

close_canvas()