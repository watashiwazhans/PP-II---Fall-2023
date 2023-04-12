import pygame as pg
rad = 30
x, y = 30, 30
done = False 
is_ball = True
pg.init()
screen = pg.display.set_mode((600,600))
clock = pg.time.Clock()
pg.display.set_caption("Ball task")

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True 
        #управление
        pressed = pg.key.get_pressed()
        if pressed[pg.K_UP]: y -= 30
        if pressed[pg.K_DOWN]: y += 30
        if pressed[pg.K_LEFT]: x -= 30
        if pressed[pg.K_RIGHT]: x += 30
        screen.fill((0, 0, 0))

        #менять цвет мяча
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            is_ball = not is_ball
        if is_ball: color = (0, 128, 255)
        else: color = (255, 100, 0)
        #мячь 
        pg.draw.circle(screen, color, (x, y), rad)
        pg.display.flip()
        clock.tick(60)
        #boundaries
        if x < 30 : x+=30
        elif x > 600 - 10: x -= 30
        elif y < 30: y += 30
        elif y > 600 - 10: y -= 30
        
