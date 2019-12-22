import pygame
from pygame.math import Vector2
import math
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, color, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = gamepygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64, 64))
        self.image.fill(color)
        self.x, self.y = x, y
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = self.x, self.y
        self.speedy, self.speedx = 0, 0 

    def update(self):
        self.rotate()
        self.speedy, self.speedx = 0, 0 
        keystate = pygame.key.get_pressed() 
        if keystate[pygame.K_w] or keystate[pygame.K_UP]:
            self.speedy = -10
        if keystate[pygame.K_s] or keystate[pygame.K_DOWN]:
            self.speedy = 10
        if keystate[pygame.K_a] or keystate[pygame.K_LEFT]:
            self.speedx = -10
        if keystate[pygame.K_d] or keystate[pygame.K_RIGHT]:
            self.speedx = 10
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT 
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
           self.rect.right = WIDTH 


class Wall:
    pass        
