import constants as const
import game
import pygame
# pygame.init()


# helpful pushing text to screen function
def toScreen(words, font, colour, x, y):
    text = font.render(words, True, colour)
    textRect = text.get_rect()
    textRect.center = (x, y)
    const.screen.blit(text, textRect)


# versions to push more than 1 line
def toScreen2(words1, words2, font, colour, x, y):
    toScreen(words1, font, colour, x, y - font.get_height() // 2)
    toScreen(words2, font, colour, x, y + font.get_height() // 2)


def toScreen3(words1, words2, words3, font, colour, x, y):
    toScreen(words1, font, colour, x, y - font.get_height())
    toScreen(words2, font, colour, x, y)
    toScreen(words3, font, colour, x, y + font.get_height())

#so that he coordinate is the top left not the center
def toScreenTopLeft(words, font, colour, x, y):
    text = font.render(words, True, colour)
    const.screen.blit(text, (x, y))

def imageToScreen(imageName, x, y, width, height):
    image = pygame.image.load(imageName)
    image = pygame.transform.scale(image, (width, height))
    const.screen.blit(image, (x, y))


def checkCoords(coords):
    for coord in coords:
        if [game.map.x, game.map.y] == coord["absolute"]:
            # print("coords exist")
            return True
    return False


def findCoordIndex(coords):
    for i, coord in enumerate(coords):
        if [game.map.x, game.map.y] == coord["absolute"]:
            # print("found at index", i)
            return i
    return -1


# directions can be top, bottom, right, left
def isAllowedToMoveToDest(direction):
    restrictedDirections = []

    for coord in const.LEFT_COORDS:
        if (game.map.x, game.map.y) == (coord[0], coord[1]):
            restrictedDirections.append("left")
            break

    for coord in const.RIGHT_COORDS:
        if (game.map.x, game.map.y) == (coord[0], coord[1]):
            restrictedDirections.append("right")
            break

    for coord in const.TOP_COORDS:
        if (game.map.x, game.map.y) == (coord[0], coord[1]):
            restrictedDirections.append("top")
            break

    for coord in const.BOTTOM_COORDS:
        if (game.map.x, game.map.y) == (coord[0], coord[1]):
            restrictedDirections.append("bottom")
            break

    if direction in restrictedDirections:
        return False

    return True


def getActualGridSize():
    return const.GRID_SIZE * const.GRID_SCALING
