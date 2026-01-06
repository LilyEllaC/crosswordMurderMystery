import pygame
import json

DEV_MODE = False
WIDTH, HEIGHT = 900, 600
FPS = 30
FPS_SCALING = 30 / FPS
GAME_ENDED_EVENT = pygame.USEREVENT + 1
TIME_IN_SECONDS = 300

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Grid related
GRID_SIZE = 32
GRID_SCALING = 2
LEFT_COORDS = list()
RIGHT_COORDS = list()
TOP_COORDS = list()
BOTTOM_COORDS = list()


def reevalConstants(coords):
    LEFT_COORDS.clear()
    RIGHT_COORDS.clear()
    TOP_COORDS.clear()
    BOTTOM_COORDS.clear()

    for coord in coords["left"]:
        LEFT_COORDS.append((coord["absolute"][0], coord["absolute"][1]))
    for coord in coords["right"]:
        RIGHT_COORDS.append((coord["absolute"][0], coord["absolute"][1]))
    for coord in coords["top"]:
        TOP_COORDS.append((coord["absolute"][0], coord["absolute"][1]))
    for coord in coords["bottom"]:
        BOTTOM_COORDS.append((coord["absolute"][0], coord["absolute"][1]))


try:
    with open("coords.json", "r") as f:
        existingCoords = json.load(f)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Warning: Could not load coords.json: {e}")
    existingCoords = {"left": [], "right": [], "top": [], "bottom": []}

reevalConstants(existingCoords)

# colours
RED = (255, 0, 0)
DARK_RED = (137, 0, 0)
ORANGE = (255, 137, 0)
DARK_ORANGE = (137, 68, 0)
YELLOW = (255, 255, 0)
DARK_YELLOW = (137, 137, 0)
GREEN = (0, 230, 15)
LIGHT_GREEN = (125, 255, 125)
DARK_GREEN = (0, 150, 0)
TEAL = (55, 225, 250)
DARK_TEAL = (0, 137, 137)
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 170)
LIGHT_BLUE = (0, 230, 255)
PURPLE = (179, 0, 255)
DARK_PURPLE = (100, 0, 150)
MAGENTA = (255, 0, 255)
DARK_MAGENTA = (137, 0, 137)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (177, 177, 177)
DARK_GRAY = (100, 100, 100)


pygame.font.init()
# fonts/font sizes
FONT_TYPE = "w.ttf"
FONT10 = pygame.font.Font(FONT_TYPE, 10)
FONT15 = pygame.font.Font(FONT_TYPE, 15)
FONT17 = pygame.font.Font(FONT_TYPE, 17)
FONT20 = pygame.font.Font(FONT_TYPE, 20)
FONT25 = pygame.font.Font(FONT_TYPE, 25)
FONT30 = pygame.font.Font(FONT_TYPE, 30)
FONT37 = pygame.font.Font(FONT_TYPE, 37)
FONT40 = pygame.font.Font(FONT_TYPE, 40)
FONT60 = pygame.font.Font(FONT_TYPE, 60)
FONT200 = pygame.font.Font(FONT_TYPE, 200)
