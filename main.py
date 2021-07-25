import pygame as pg

pg.init()
clock = pg.time.Clock()
FPS = 60

x, y = 0, 0
pos = [x, y]
green_color = pg.Color(0, 255, 127)
size = (300, 300)
screen = pg.display.set_mode(size)

per = False
run = True
prev_pos = ()

while run:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = prev_pos = new_pos = pg.mouse.get_pos()
            if pos[0] <= new_pos[0] <= pos[0] + 70 and pos[1] <= new_pos[1] <= pos[1] + 70:
                per = True
        if event.type == pg.MOUSEBUTTONUP:
            per = False
        if event.type == pg.MOUSEMOTION and per == True:
            new_pos = pg.mouse.get_pos()
            pos[0] = pos[0] + new_pos[0] - prev_pos[0]
            pos[1] = pos[1] + new_pos[1] - prev_pos[1]
            prev_pos = new_pos
        if event.type == pg.QUIT:
            run = False

    screen.fill((0, 0, 0))
    pg.draw.rect(screen, green_color, (pos, (70, 70)))
    pg.display.flip()

    clock.tick(FPS)

pg.quit()