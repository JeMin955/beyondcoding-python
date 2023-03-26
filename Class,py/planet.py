from turtle import Screen
import pygame
import pymunk
import math
import pygame
import random

import pymunk.pygame_util

def planetGravity(body, gravity, damping, dt):
    sq_dist = body.position.get_dist_sqrd((300, 300))
    g = (
        (body.position - pymunk.Vec2d((300, 300))) * -5.0e6 / (sq_dist * math.sqrt(sq_dist))
    )
    pymunk.Body.update_velocity(body, g, damping, dt)

def add_box(space):
    body = pymunk.Body()
    body.position = pymunk.Vec2d(random.randint(50, 550), random.radint(50,550))
    body.velocity_func = planetGravity

pygame.init()

screen = pygame.display.set_mode([600, 600])
clock = pygame.time.Clock()

space = pymunk.Space()

draw_options = pymunk.pygame_util.DrawOptions(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill(pygame.Color("black"))

    pygame.draw.circle(screen, pygame.Color("yellow"), (300, 300), 10)

    pygame.display.flip()
    clock.tick()