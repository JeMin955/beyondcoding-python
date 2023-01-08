import pygame as pg
pg.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)

SIZE = [600, 600]

screen = pg.display.set_mode(SIZE)
pg.display.set_caption()

playing = True
clock = pg.time.Clock()

while playing:
    clock.tick(120)

    event = pg.event.poll()
    if event.type == pg.QUIT:
        playing = False

pg.quit()