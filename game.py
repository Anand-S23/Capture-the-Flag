import pygame 
import random
import math
import sys
from os import path
#from game_objects import *  
from settings import *

img_dir = path.join(path.dirname(__file__), 'graphics')

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Cap the Flag')
clock = pygame.time.Clock()


right = pygame.sprite.Group()
left = pygame.sprite.Group()
flags = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color, side):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.xi, self.yi = x, y
        self.side = side
        self.vx, self.vy = 0, 0
        self.flag_picked = False
        self.score = 0

    def reset(self):
        self.x = self.xi
        self.y = self.yi

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pygame.key.get_pressed()
        if self.side == 'left':
            if keys[pygame.K_a]:
                self.vx = -PLAYER_SPEED
            if keys[pygame.K_d]:
                self.vx = PLAYER_SPEED
            if keys[pygame.K_w]:
                self.vy = -PLAYER_SPEED
            if keys[pygame.K_s]:
                self.vy = PLAYER_SPEED
        if self.side == 'right':
            if keys[pygame.K_LEFT]:
                self.vx = -PLAYER_SPEED
            if keys[pygame.K_RIGHT]:
                self.vx = PLAYER_SPEED
            if keys[pygame.K_UP]:
                self.vy = -PLAYER_SPEED
            if keys[pygame.K_DOWN]:
                self.vy = PLAYER_SPEED

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pygame.sprite.spritecollide(self, walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pygame.sprite.spritecollide(self, walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y

    def update(self):
        self.get_keys()
        self.x += self.vx 
        self.y += self.vy 
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * 32
        self.rect.y = y * 32

class Flag(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y

    def hide(self):
        self.rect.x = -64
    
    def show(self, flag):
        if flag == 'left':
            self.rect.x = 68
        if flag == 'right':
            self.rect.x = WIDTH - 100

def start_menu():
    running = True 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

def login_screen():
    running = True 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

def register_screen():
    running = True 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

def account():
    running = True 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = Falses

def load_map(file):
    game_folder = path.dirname(__file__)
    map_data = []
    with open(path.join(game_folder, "maps/map.txt"), 'rt') as f:
        for line in f:
            map_data.append(line)

    for row, tiles in enumerate(map_data):
        for col, tile in enumerate(tiles):
            if tile == '1':
                wall = Wall(col, row)
                walls.add(wall)
                all_sprites.add(wall)


def game():
    player_left = Player(120, HEIGHT / 2, RED, 'left')
    player_right = Player(WIDTH - 152, HEIGHT / 2, BLUE, 'right')
    flag_left = Flag(68, HEIGHT / 2)
    flag_right = Flag(WIDTH - 100, HEIGHT / 2)

    right.add(flag_right)
    left.add(flag_left)
    all_sprites.add(flag_left, flag_right, player_left, player_right)

    load_map('maps/map.txt')
    
    background = pygame.image.load(path.join(img_dir, 'background.png')).convert()
    background_rect = background.get_rect()

    # Game loop 
    running = True 
    while running:
        # Setting the FPS 
        clock.tick(FPS)

        hit = pygame.sprite.collide_rect(player_left, player_right)
        left_picked = pygame.sprite.spritecollide(player_right, left, False)
        right_picked = pygame.sprite.spritecollide(player_left, right, False)

        if hit:
            if player_left.rect.x < WIDTH / 2 and player_right.rect.x < WIDTH / 2:
                if not (player_right.rect.x < 50): 
                    if player_right.flag_picked == True:
                        player_right.flag_picked = False
                        flag_left.show('left')
                    player_right.reset()
                
            elif player_left.rect.x > WIDTH / 2 and player_right.rect.x > WIDTH / 2:
                if not (player_left.rect.x > WIDTH - 72): 
                    if player_left.flag_picked == True:
                        player_left.flag_picked = False
                        flag_right.show('right')
                    player_left.reset()
                    
        if right_picked:
            flag_right.hide()
            player_left.flag_picked = True
        
        if left_picked: 
            flag_left.hide()
            player_right.flag_picked = True

        if player_left.flag_picked == True and player_left.rect.x < 64:
                player_left.flag_picked = False
                flag_right.show('right')
                player_left.score += 1

        if player_right.flag_picked == True and player_right.rect.x > WIDTH - 100:
                player_right.flag_picked = False
                flag_left.show('left')
                player_right.score += 1

        # Process input (events)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update 
        all_sprites.update()
            
        # Draw / Render
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        pygame.display.flip()

game()
pygame.quit()
