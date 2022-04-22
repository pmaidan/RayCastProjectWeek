from settings import *
import pygame
import math
from map import collision_walls


class Player:
    def __init__(self):
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.side = 50
        self.rect = pygame.Rect(PLAYER_POS[0], PLAYER_POS[1], self.side, self.side)

    @property
    def pos(self):
        return self.x, self.y

    def detect_collision(self, dx, dy):
        next_rect = self.rect.copy()
        next_rect.move_ip(dx, dy)
        hit_idxs = next_rect.collidelistall(collision_walls)

        if len(hit_idxs) > 0:
            delta_x, delta_y = 0, 0
            for hit_idx in hit_idxs:
                hit_rect = collision_walls[hit_idx]
                if dx > 0:
                    delta_x += next_rect.right - hit_rect.left
                else:
                    delta_x += hit_rect.right - next_rect.left
                if dy > 0:
                    delta_y += next_rect.bottom - hit_rect.top
                else:
                    delta_y += hit_rect.bottom - next_rect.top

            if abs(delta_x - delta_y) < 10:
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_y > delta_x:
                dx = 0
        self.x += dx
        self.y += dy

    def movement(self):
        self.keys_control()
        self.rect.center = self.x, self.y

    def keys_control(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            dx = PLAYER_SPEED * cos_a
            dy = PLAYER_SPEED * sin_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_s]:
            dx = - PLAYER_SPEED * cos_a
            dy = - PLAYER_SPEED * sin_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_a]:
            dx = PLAYER_SPEED * sin_a
            dy = - PLAYER_SPEED * cos_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_d]:
            dx = - PLAYER_SPEED * sin_a
            dy = PLAYER_SPEED * cos_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_LEFT]:
            self.angle -= ANGLE_SPEED
        if keys[pygame.K_RIGHT]:
            self.angle += ANGLE_SPEED
