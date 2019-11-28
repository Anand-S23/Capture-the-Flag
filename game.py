import pygame 
import random
import math
import time
from os import path
from player import Player
from settings import *

# initalize pygame and create window 
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Capture the flag')
clock = pygame.time.Clock()

player = Player(red, width/2, height/2) #player testing

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Game loop 
running = True 
while running:
    # Setting the fps 
    clock.tick(fps)

    # Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update 
    all_sprites.update()

    # Draw / Render
    screen.fill(dark_gray)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()