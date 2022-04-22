import pygame
from settings import *
import math


class Button:
    def __init__(self, sc, sc_type):
        self.img = PLAY_BUTTON
        self.rect = self.img.get_rect()
        self.x, self.y = (WIN_HALF_WIDTH - self.rect.w // 2, WIN_HALF_HEIGHT - self.rect.h)
        self.sc = sc
        self.timer = 0

        self.sc_type = sc_type

    def draw(self):
        self.sc.blit(self.img, (self.x, self.y))

    def update(self):
        self.timer += 1
        self.y = VICTORY_POS[1] + math.sin(self.timer * 100) * 5
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and self.sc_type == 'menu':
            if self.x < mouse_pos[0] < self.x + self.rect.w and self.y < mouse_pos[1] < self.y + self.rect.h:
                self.sc_type = 'game'
