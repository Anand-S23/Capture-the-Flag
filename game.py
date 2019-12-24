import pygame 
import random
import math
import time
import sys
from os import path
from game_objects import *  
from settings import *
import datetime

img_dir = path.join(path.dirname(__file__), 'graphics')

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Cap the Flag')
clock = pygame.time.Clock()


right = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()

player_left = RedPlayer()
player_right = BluePLayer()
wall1 = Wall(100, 100, 60, 30)

right.add(player_right)
all_sprites.add(player_left, player_right, wall1)
walls.add(wall1)

background = pygame.image.load(path.join(img_dir, 'background.png')).convert()
background_rect = background.get_rect()

# Game loop 
running = True 
while running:
    # Setting the FPS 
    clock.tick(FPS)

    hit = pygame.sprite.spritecollide(player_left, right, False)

    if hit:
        if player_left.rect.x < WIDTH / 2 and player_right.rect.x < WIDTH / 2:
            player_right.reset()
            
        elif player_left.rect.x > WIDTH / 2 and player_right.rect.x > WIDTH / 2:
            player_left.reset()

            
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

pygame.quit()