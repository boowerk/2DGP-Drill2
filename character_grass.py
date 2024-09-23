from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 100
y = 90
while (x < 300):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    x += 2
    delay(0.01)


while (y < 190):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    x -= 2
    y += 2
    delay(0.01)
    
while (x > 100):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    x -= 2
    y -= 2
    delay(0.01)

close_canvas()
