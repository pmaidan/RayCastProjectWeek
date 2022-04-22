import pygame
from settings import *
from player import Player
import math
from map import world_map
from ray_casting import ray_casting
from drawing import Drawing
from menu import *


def main():
    pygame.init()
    sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    sc_type = 'menu'
    clock = pygame.time.Clock()

    player = Player()
    drawing = Drawing(sc)
    button = Button(sc, sc_type)

    do_game = True
    while do_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                do_game = False

        player.movement()

        button.update()
        sc_type = button.sc_type

        sc.fill(COLOR_BLACK)

#        for x, y in world_map:
#            pygame.draw.rect(sc, COLOR_GRAY, (x, y, MAP_TILE, MAP_TILE), 2)

        if sc_type == 'game':
            drawing.background(player.angle)
            drawing.world(player.pos, player.angle)
            drawing.fps(clock)
        else:
            drawing.menu(button)

#        pygame.draw.circle(sc, COLOR_GREEN, player.pos, PLAYER_SIZE)
#        pygame.draw.line(sc, COLOR_GREEN, player.pos, (player.x + WIN_WIDTH * math.cos(player.angle),
#                                                       player.y + WIN_WIDTH * math.sin(player.angle)))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
