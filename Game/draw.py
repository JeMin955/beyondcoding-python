from turtle import distance
import pygame as pg
import time as t
import random as r
import math as mt
pg.init()

white = (255, 255, 255)
red = (255, 0, 0)
green = (100, 250, 100)
blue = (0, 0, 250)
black = (0, 0, 0)
manggo = (255, 202, 24)
purple = (184, 61, 186)

size = [800, 600]
screen = pg.display.set_mode(size)
pg.display.set_caption("JaeMin's game")

x_pos, y_pos = size[0]/2, size[1]/2
x_coor, y_coor = size[0]/2, size[1]/2

circle1_color = (255, 0, 0)
circle2_color = (0, 0, 255)

screen.fill((253, 116, 255))

def collision_check():
    distance = mt.sqrt((x_pos - x_coor)**2 + (y_pos - y_coor)**2)
    if distance < 40:
        return True
    return False

playing = True
clock = pg.time.Clock()

while playing:
    
    clock.tick(200)

    event = pg.event.poll()
    if event.type == pg.QUIT:
        playing = False

    pressed = pg.key.get_pressed()
    if pressed[pg.K_w]:
        y_pos -= 1
    if pressed[pg.K_s]:
        y_pos += 1
    if pressed[pg.K_a]:
        x_pos -= 1
    if pressed[pg.K_d]:
        x_pos += 1

    pressed = pg.key.get_pressed()
    if pressed[pg.K_UP]:
        y_coor -= 1
    if pressed[pg.K_DOWN]:
        y_coor += 1
    if pressed[pg.K_LEFT]:
        x_coor -= 1
    if pressed[pg.K_RIGHT]:
        x_coor += 1

    pg.draw.circle(screen, (circle1_color), [x_pos, y_pos], 20, 0)
    pg.draw.circle(screen, (circle2_color), [x_coor, y_coor], 20, 0)
    
    if collision_check():
        r = red[0] + blue[0]
        if r > 255:
            r = 255
        g = red[1] + blue[1]
        if g > 255:
            g = 255
        b = red[2] + blue[2]
        if b > 255:
            b = 255

        circle1_color = circle2_color = (r, g, b)
    else:
        circle1_color = red
        circle2_color = blue

    pg.display.update()

pg.quit()
