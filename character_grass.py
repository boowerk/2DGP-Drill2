from pico2d import *
import math 

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while (1):
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

    center_x = 400
    center_y = 300
    radius = 200

    angle = 0

    while (angle < 360):
        clear_canvas_now()
        grass.draw_now(400, 30)    
        
        x = center_x + radius * math.cos(math.radians(angle))
        y = center_y + radius * math.sin(math.radians(angle))
        character.draw_now(x, y)

        angle += 1
        delay(0.01)



close_canvas()
