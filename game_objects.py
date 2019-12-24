import pygame
from pygame.math import Vector2
import math
from settings import *

class RedPlayer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = 120
        self.rect.centery = HEIGHT / 2
        self.speedy = 0

    def reset(self):
        self.rect.centerx = 120
        self.rect.centery = HEIGHT / 2

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

    def reset(self):
        self.rect.centerx = WIDTH - 120
        self.rect.centery = HEIGHT / 2

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

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, height, width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((height, width))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
