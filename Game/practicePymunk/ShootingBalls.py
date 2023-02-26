from email.quoprimime import body_check
from sqlite3 import SQLITE_DROP_TEMP_INDEX
import pyglet
from pyglet.window import key

import pymunk
import pymunk.pyglet_util
from pymunk import Vec2d

class Main(pyglet.window.Window):
    def __init__(self):

        pyglet.window.Window.__init__(self, vsync=False)
        self.set_caption("Shooting Balls")

        pyglet.clock.schedule_interval(self.update, 1 / 60)
        self.fps_display = pyglet.window.FPSDisplay(self)

        self.text = pyglet.text.Label(
            "Press space to fire bullet", font_size=30, x=15, y=400
        )
        self.create_world()

        self.draw_options = pymunk.pyglet_util.DrawOptions()
        self.draw_options.flags = self.draw_options.DRAW_SHAPES

    def create_world(self):
        self.space = pymunk.Space()
        self.space.gravity = Vec2d(0, -900)

        static_lines = [
            pymunk.Segment(self.space.static_body, Vec2d(20, 55), Vec2d(600, 55), 1),
            pymunk.Segment(self.space.static_body, Vec2d(550, 55), Vec2d(550, 400), 1),

        ]

        for l in static_lines:
            l.friction = 0.3
        self.space.add(*static_lines)

        for x in range(5):
            for y in range(10):
                size = 20
                mass = 10
                moment = pymunk.moment_for_box(mass, (size, size))
                body = pymunk.Body(mass, moment)
                body.position = Vec2d(300 + x * 50, 105 + y * (size + 0.1))
                shape = pymunk.Poly.create_box(body, (size, size))
                shape.friction = 0.3
                self.space.add(body, shape)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            mass = 100
            r = 14
            moment = pymunk.moment_for_circle(mass, 0, r, (0, 0))
            body = pymunk.Body(mass, moment)
            body.position = (0, 165)
            shape = pymunk.Circle(body, r , (0, 0))
            shape.friction = 0.3
            shape.color = (255, 255, 255, 125)
            self.space.add(body, shape)
            f = 1000000
            body.apply_impulse_at_local_point((f /5, f / -15), (0, 0))
        elif symbol == key.ESCAPE:
            pyglet.app.exit()


    def update(self, dt):
        step_dt = 1 / 250
        x = 0
        while x < dt:
            x += step_dt
            self.space.step(step_dt)

    def on_draw(self):
        self.clear()
        self.text.draw()
        self.fps_display.draw()
        self.space.debug_draw(self.draw_options)

main = Main()
pyglet.app.run()