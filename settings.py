import math
import pygame

# window settings
WIN_WIDTH = 1200
WIN_HEIGHT = 800
WIN_HALF_WIDTH = WIN_WIDTH // 2
WIN_HALF_HEIGHT = WIN_HEIGHT // 2
test_display = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

# colors
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (150, 0, 0)
COLOR_GREEN = (0, 220, 0)
COLOR_BLUE = (0, 0, 50)
COLOR_GRAY = (110, 110, 110)
COLOR_PURPLE = (120, 0, 120)
COLOR_YELLOW = (40, 30, 10)

# rendering settings
FPS = 60
FPS_POS = WIN_WIDTH - 65, 5

# player settings
PLAYER_POS = (2100 + 0.00000001, 400 + 0.00000001)
PLAYER_ANGLE = 0
PLAYER_SPEED = 2
PLAYER_SIZE = 12
ANGLE_SPEED = 0.02

# map settings
MAP_TILE = WIN_WIDTH // 12

# texture settings
TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
TEXTURE_SCALE = TEXTURE_WIDTH // MAP_TILE

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 400
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 2 * DIST * MAP_TILE
SCALE = WIN_WIDTH // NUM_RAYS

# menu
VICTORY_POS = (20, WIN_HALF_HEIGHT)
MENU_BG = pygame.image.load('er.menu.png').convert()
PLAY_BUTTON = pygame.image.load('er.play.button.png').convert_alpha()
