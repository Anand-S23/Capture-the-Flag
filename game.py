import pygame 
import random
import math
import time
from os import path

width = 800
height = 600
fps = 30

# initalize pygame and create window 
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Capture the flag')
clock = pygame.time.Clock()


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
        
    # Draw / Render
    screen.fill((255,255,255))
    pygame.display.flip()

pygame.quit()