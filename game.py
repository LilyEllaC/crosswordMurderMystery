from time import strftime

import constants as const
import pygame
import sprites
import utility
import datetime

map = sprites.Objects(0 + (-320), 6 + (-1050), 992 * 2, 736 * 2, "assets/map.png")
player = sprites.Player(const.WIDTH / 2, const.HEIGHT / 2, 64, 64)
startTime = None

leftSquares = []
rightSquares = []
topSquares = []
bottomSquares = []

leftSquareColor = (0, 255, 0)
rightSquareColor = (255, 0, 0)
topSquareColor = (0, 0, 255)
bottomSquareColor = (255, 255, 0)

leftSquareSurface = pygame.Surface((32, 32))
leftSquareSurface.set_alpha(128)
leftSquareSurface.fill(leftSquareColor)

rightSquareSurface = pygame.Surface((32, 32))
rightSquareSurface.set_alpha(128)
rightSquareSurface.fill(rightSquareColor)

topSquareSurface = pygame.Surface((32, 32))
topSquareSurface.set_alpha(128)
topSquareSurface.fill(topSquareColor)

bottomSquareSurface = pygame.Surface((32, 32))
bottomSquareSurface.set_alpha(128)
bottomSquareSurface.fill(bottomSquareColor)

crosswordButton=sprites.Button(10, 10, 200, 50, "Crossword", const.FONT37, const.GREEN, const.DARK_GREEN, True)

def showGame():
    const.screen.fill(const.BLACK)
    map.draw()
    crosswordButton.draw()
    crosswordButton.isHovered()
    player.draw()

    s = pygame.Surface((80, 40), pygame.SRCALPHA)  # per-pixel alpha
    s.fill((255, 255, 255, 128))  # notice the alpha value in the color
    const.screen.blit(s, (const.WIDTH - 90, const.HEIGHT - 45))

    if startTime is not None:
        seconds_left = const.TIME_IN_SECONDS if not startTime else int(
            max(0, const.TIME_IN_SECONDS - (datetime.datetime.now() - startTime).total_seconds()))
        formatted = "{:d}:{:02d}".format(*divmod(seconds_left, 60))
        utility.toScreen(formatted, const.FONT37, const.BLACK, const.WIDTH - 50, const.HEIGHT - 30)

        if seconds_left == 0:
            pygame.event.post(pygame.event.Event(const.GAME_ENDED_EVENT))

    for square_x, square_y in leftSquares:
        const.screen.blit(leftSquareSurface, (map.x + square_x, map.y + square_y))

    for square_x, square_y in rightSquares:
        const.screen.blit(rightSquareSurface, (map.x + square_x, map.y + square_y))

    for square_x, square_y in topSquares:
        const.screen.blit(topSquareSurface, (map.x + square_x, map.y + square_y))

    for square_x, square_y in bottomSquares:
        const.screen.blit(bottomSquareSurface, (map.x + square_x, map.y + square_y))
