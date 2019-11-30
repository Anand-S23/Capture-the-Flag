import pygame
from pygame.math import Vector2
import math
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(color)
        self.original_image = self.image
        self.x, self.y = x, y
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.speedy = 0
        self.speedx = 0

    def update(self):
        self.rotate()
        self.speedy = 0
        self.speedx = 0 
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
        elif self.rect.bottom > height:
            self.rect.bottom = height 
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > width:
           self.rect.right = width 

        
    def rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.image = pygame.transform.rotate(self.original_image, int(angle))
        self.rect = self.image.get_rect(center=self.position)