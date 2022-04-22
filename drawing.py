import pygame
from settings import *
from ray_casting import ray_casting
from map import LEVEL_END
from menu import *


class Drawing:
    def __init__(self, sc):
        self.sc = sc
        self.font = pygame.font.SysFont('georgia', 40)
        self.textures = {1: pygame.image.load('wall.png').convert(),
                         'S': pygame.image.load('sky.jpeg').convert(),
                         'P': pygame.image.load('panel.png').convert_alpha()
                         }

    def menu(self, button):
        self.sc.blit(MENU_BG, (0, 0))
        button.draw()

    def background(self, angle):
        sky_offset = -5 * math.degrees(angle) % WIN_WIDTH
        self.sc.blit(self.textures['S'], (sky_offset, 0))
        self.sc.blit(self.textures['S'], (sky_offset - WIN_WIDTH, 0))
        self.sc.blit(self.textures['S'], (sky_offset + WIN_WIDTH, 0))
#        pygame.draw.rect(self.sc, COLOR_BLUE, (0, 0, WIN_WIDTH, WIN_HALF_HEIGHT))
        pygame.draw.rect(self.sc, COLOR_YELLOW, (0, WIN_HALF_HEIGHT, WIN_WIDTH, WIN_HALF_HEIGHT))

    def world(self, player_pos, player_angle):
        ray_casting(self.sc, player_pos, player_angle, self.textures)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, COLOR_RED)
        self.sc.blit(render, FPS_POS)

    def victory(self, player):
        if player.x // MAP_TILE * MAP_TILE == LEVEL_END[0] and player.y // MAP_TILE * MAP_TILE == LEVEL_END[1]:
            self.sc.blit(self.textures['P'], VICTORY_POS)
            display_victory = 'YOU WON!'
            render = self.font.render(display_victory, 0, COLOR_RED)
            self.sc.blit(render, VICTORY_POS)
