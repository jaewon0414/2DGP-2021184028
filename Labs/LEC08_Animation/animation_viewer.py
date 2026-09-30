from pico2d import *

WIDTH, HEIGHT = 800, 600

open_canvas(WIDTH, HEIGHT)

hero = load_image('hero_sheet.png')

clear_canvas()
hero.draw(WIDTH // 2, HEIGHT // 2)
update_canvas()

delay(1)

close_canvas()
