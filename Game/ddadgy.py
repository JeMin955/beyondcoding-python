import pygame as pg
import time as t
import random as r
pg.init()

white = (255, 255, 255)
red = (255, 100, 100)
green = (100, 250, 100)
blue = (100, 100, 250)
black = (0, 0, 0)
manggo = (150, 100, 100)

size = [1710, 1050]
screen = pg.display.set_mode(size)
pg.display.set_caption("PYthoN")

class Box:
    def __init__(self, x_pos, y_pos, width, height, color, speed):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

class Player(Box):
    def __init__(self, x_pos, y_pos, width, height, color, speed):
        super().__init__(x_pos, y_pos, width, height, color, speed)

class Enemy(Box):
    def __init__(self, screen_size, width, height, color, speed):
        spawn_point = self.spawn(screen_size, width, height)
        super().__init__(*spawn_point, width, height, color, speed)

    def chase(self, player):
        if player.x_pos > self.x_pos:
            self.x_pos += self.speed
        elif player.x_pos < self.x_pos:
            self.x_pos -= self.speed
        if player.y_pos > self.y_pos:
            self.y_pos += self.speed
        elif player.y_pos < self.y_pos:
            self.y_pos -= self.speed

    def spawn(self, screen_size, width, height):
        spawn_points = [
            [0, r.randint(0, screen_size[1] - height)],
            [screen_size[0] - width, r.randint(0, screen_size[1] - height)],
            [r.randint(0, screen_size[0] - width), 0],
            [r.randint(0, screen_size[0] - width), screen_size[1] - height]
        ]
        return r.choice(spawn_points)
   
def check_collision(player, enemy):
    if abs(player.x_pos - enemy.x_pos) < player.width and abs(player.y_pos - enemy.y_pos) < player.height:
        return True
    return False

def write(screen, string, font, size, centerx, centery, color):
    font = pg.font.SysFont(font, size, True, False)
    text = font.render(string, True, color)
    text_box = text.get_rect()
    text_box.centerx = centerx
    text_box.centery = centery

    screen.blit(text, text_box)

player = Player(size[0]/2-85/2, size[1]/2-60/2, 40, 40, white, 7)
#enemy = Enemy(screen.get_size(), 40, 40, red, 3)
print(player)
to_x, to_y = 0,0

enemies = []
for i in range(15):
    enemies.append(Enemy(screen.get_size(), 40, 40, red, 0.5))

enemy_spawn_time = 2
enemy_spawn_count = 0
start_time = t.time()

playing = True
clock = pg.time.Clock()

while playing:

    clock.tick(200)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:

                to_y -= player.speed
            elif event.key == pg.K_DOWN:

                to_y += player.speed
            elif event.key == pg.K_LEFT:

                to_x -= player.speed
            elif event.key == pg.K_RIGHT:

                to_x +=player.speed

        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:

                to_y = 0
            elif event.key == pg.K_DOWN:

                to_y = 0
            elif event.key == pg.K_LEFT:

                to_x =0
            elif event.key == pg.K_RIGHT:

                to_x =0

    if player.x_pos + to_x < size[0]-80 and player.x_pos + to_x > 0:
        player.x_pos += to_x

    if player.y_pos + to_y < size[1]-80 and player.y_pos + to_y > 0:
        player.y_pos += to_y

    screen.fill(black)
    # pg.draw.circle(screen, manggo, [size[0]/2, size[1]/2], 50, 0)
    pg.draw.rect(screen, player.color, [player.x_pos, player.y_pos, player.width, player.height], 5)

    if event.type == pg.QUIT:
        playing = False

    survival_time = str(round(t.time() - start_time, 2))
    write(screen, survival_time, "arial", 30, screen.get_size()[0]/2, 50, white)

    if t.time() - start_time > enemy_spawn_time * enemy_spawn_count:
        enemies.append(Enemy(screen.get_size(), 20, 20, blue, 2))
        enemy_spawn_count += 1

    for enemy in enemies:
        enemy.chase(player)

        if check_collision(player,enemy):
            write(screen, "END", "arial", 200, screen.get_size()[0]/2, screen.get_size()[1]/2, white)            
            playing = False



        pg.draw.rect(screen, enemy.color, [enemy.x_pos, enemy.y_pos, enemy.width, enemy.height], 0)
    
    pg.display.update()

t.sleep(1.5)

pg.quit()