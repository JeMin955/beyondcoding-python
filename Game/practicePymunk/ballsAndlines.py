import pygame as pg
import pymunk as pm

from pymunk import Vec2d

X, Y = 0, 1

COLLTYPE_DEFAULT = 0
COLLTYPE_MOUSE = 1
COLLTYPE_BALL = 2

def flipy(y):
    return -y + 600

def mouse_coll_func(arbiter, space, data):
    return False

def main():
    pg.init()
    screen = pg.display.set_mode((600, 600))

    clock = pg.time.Clock()
    running = True

    space = pm.Space()
    space.gravity = 0.0, -900.0

    balls = []

    mouse_body = pm.Body(body_type = pm.Body.KINEMATIC)
    mouse_shape = pm.Circle(mouse_body, 3, (0, 0))

    space.add(mouse_body, mouse_shape)

    space.add_collision_handler(
        COLLTYPE_MOUSE, COLLTYPE_BALL
    ).pre_solve = mouse_coll_func

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                p = event.pos[X], flipy(event.pos[Y])
                body = pm.Body(10, 100)
                body.position = p

                shape = pm.Circle(body, 10, p)
                shape.friction = 0.5

                shape.collition_type = COLLTYPE_BALL
                space.add(body, shape)
                balls.append(shape)

        p = pg.mouse.get_pos()
        mouse_pos = Vec2d(p[X], flipy(p[Y]))
        mouse_body.position = mouse_pos

        if pg.key.get_mods() & pg.KMOD_SHIFT and pg.mouse.get_pressed()[0]:
            body = pm.Body(10, 100)
            body.position = mouse_pos

            shape = pm.Circle(body, 10, mouse_pos)
            shape.friction = 0.5

            shape.collition_type = COLLTYPE_BALL
            space.add(body, shape)
            balls.append(shape)
            
        dt = 1 / 60
        space.step(dt)

        screen.fill(pg.Color("white"))

        for ball in balls:
            r = ball.radius
            v = ball.body.position

            rot = ball.body.rotation_vector
            p = int(v.x), int(flipy(v.y))
            p2 = p + Vec2d(rot.x, -rot.y) * r * 0.9
            p2 = int(p2.x), int(p2.y)

            pg.draw.circle(screen, pg.Color("blue"), p, int(r), 2)
            pg.draw.line(screen, pg.Color("red"), p, p2)

        pg.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()