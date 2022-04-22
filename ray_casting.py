import pygame
from settings import *
from map import world_map, WORLD_WIDTH, WORLD_HEIGHT


# def ray_casting(sc, player_pos, player_angle):
#     cur_angle = player_angle - HALF_FOV
#     xo, yo = player_pos
#     for ray in range(NUM_RAYS):
#         sin_a = math.sin(cur_angle)
#         cos_a = math.cos(cur_angle)
#         for depth in range(MAX_DEPTH):
#             x = xo + depth * cos_a
#             y = yo + depth * sin_a
#             if (x // MAP_TILE * MAP_TILE, y // MAP_TILE * MAP_TILE) in world_map:
#                 depth *= math.cos(player_angle - cur_angle)
#                 proj_height = PROJ_COEFF / depth
#                 c = 255 / (1 + depth * depth * 0.0001)
#                 color = (c, c, c)
#                 pygame.draw.rect(sc, color, (ray * SCALE, WIN_HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
#                 break
#         cur_angle += DELTA_ANGLE


def mapping(a, b):
    return a // MAP_TILE * MAP_TILE, b // MAP_TILE * MAP_TILE


def ray_casting(sc, player_pos, player_angle, textures):
    xo, yo = player_pos
    xm, ym = mapping(xo, yo)
    xh, yv = 0, 0
    texture_h, texture_v = 0, 0
    cur_angle = player_angle - HALF_FOV
    depth_v = 0.0
    depth_h = 0.0
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        # verticals
        x, dx = (xm + MAP_TILE, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, WORLD_WIDTH, MAP_TILE):
            depth_v = (x-xo) / cos_a
            yv = yo + depth_v * sin_a
            tile_v = mapping(x + dx, yv)
            if tile_v in world_map:
                texture_v = world_map[tile_v]
                break
            x += dx * MAP_TILE

        # horizontals
        y, dy = (ym + MAP_TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, WORLD_HEIGHT, MAP_TILE):
            depth_h = (y-yo) / sin_a
            xh = xo + depth_h * cos_a
            tile_h = mapping(xh, y + dy)
            if tile_h in world_map:
                texture_h = world_map[tile_h]
                break
            y += dy * MAP_TILE

        # projection
        depth, offset, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
        offset = int(offset) % MAP_TILE
        depth *= math.cos(player_angle - cur_angle)
        proj_height = PROJ_COEFF / depth
#        c = 255 / (1 + depth * depth * 0.0005)
#        color = (c / 2, 0, c)
#        pygame.draw.rect(sc, color, (ray * SCALE, WIN_HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
        wall_column = textures[texture].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
        wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
        sc.blit(wall_column, (ray * SCALE, WIN_HALF_HEIGHT - proj_height // 2))
        cur_angle += DELTA_ANGLE
