import pygame 
import random
import math
import time
import sys
from os import path
from game_objects import *  
from settings import *
import time

'''
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(DARK_GRAY)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def events(self):
        # catch all events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()

# create the game object
g = Game()
while True:
    g.new()
    g.run()

 '''

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Cap the Flag')
clock = pygame.time.Clock()


class RedPlayer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = 120
        self.rect.centery = HEIGHT / 2
        self.speedy = 0
        self.moving = True

    def reset(self):
        self.rect.centerx = 120
        self.rect.centery = HEIGHT / 2
        start = time.time()
        self.moving = False
        while self.moving == False:
            time_diff = time.time()
            if time_diff > 5000:
                self.moving = True


    def update(self):
        self.speedy = 0
        self.speedx = 0
        keystate = pygame.key.get_pressed() 
        if keystate[pygame.K_w]:
            self.speedy = -7
        if keystate[pygame.K_s]:
            self.speedy = 7
        if keystate[pygame.K_a]:
            self.speedx = -7
        if keystate[pygame.K_d]:
            self.speedx = 7
        
        if self.moving: 
            self.rect.y += self.speedy
            self.rect.x += self.speedx

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT - 1:
            self.rect.bottom = HEIGHT - 1
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class BluePLayer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH - 120
        self.rect.centery = HEIGHT / 2
        self.speedy = 0
        self.moving = True

    def reset(self):
        self.rect.centerx = WIDTH - 120
        self.rect.centery = HEIGHT / 2
        start = time.time()
        self.moving = False
        while self.moving == False:
            time_diff = time.time()
            if time_diff > 5000000000000:
                self.moving = True

    def update(self):
        self.speedy = 0
        self.speedx = 0
        keystate = pygame.key.get_pressed() 
        if keystate[pygame.K_UP]:
            self.speedy = -7
        if keystate[pygame.K_DOWN]:
            self.speedy = 7
        if keystate[pygame.K_RIGHT]:
            self.speedx = 7
        if keystate[pygame.K_LEFT]:
            self.speedx = -7
        
        if self.moving:
            self.rect.y += self.speedy
            self.rect.x += self.speedx

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


right = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

player_left = RedPlayer()
player_right = BluePLayer()

right.add(player_right)
all_sprites.add(player_left, player_right)

sp1 = 0
sp2 = 0

# Game loop 
running = True 
while running:
    # Setting the FPS 
    clock.tick(FPS)

    hit = pygame.sprite.spritecollide(player_left, right, False)

    if hit:
        if player_left.rect.x < WIDTH / 2 and player_right.rect.x < WIDTH / 2:
            player_right.moving = False
            player_right.reset()
            print(player_right.moving)
        elif player_left.rect.x > WIDTH / 2 and player_right.rect.x > WIDTH / 2:
            player_left.moving = False
            player_left.reset()
            print(player_left.moving)

    # Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update 
    all_sprites.update()
    
        
    # Draw / Render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()