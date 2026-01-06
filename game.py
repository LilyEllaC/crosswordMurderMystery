import constants as const
import pygame
from sprites import Objects, Player

map = Objects(0 + (-320), 6 + (-1050), 992 * 2, 736 * 2, "assets/map.png")
player = Player(const.WIDTH / 2, const.HEIGHT / 2, 64, 64)

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


def show_game():
    const.screen.fill(const.BLACK)

    map.draw()
    player.draw()

    for square_x, square_y in leftSquares:
        const.screen.blit(leftSquareSurface, (map.x + square_x, map.y + square_y))

    for square_x, square_y in rightSquares:
        const.screen.blit(rightSquareSurface, (map.x + square_x, map.y + square_y))

    for square_x, square_y in topSquares:
        const.screen.blit(topSquareSurface, (map.x + square_x, map.y + square_y))

    for square_x, square_y in bottomSquares:
        const.screen.blit(bottomSquareSurface, (map.x + square_x, map.y + square_y))
