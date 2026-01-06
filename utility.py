import constants as const
import pygame
pygame.init()

#helpful pushing text to screen function
def toScreen(words, font, colour, x, y):
    text=font.render(words, True, colour)
    textRect=text.get_rect()
    textRect.center=(x, y)
    const.screen.blit(text, textRect)

#versions to push more than 1 line
def toScreen2(words1, words2, font, colour, x, y):
    toScreen(words1, font, colour, x, y-font.get_height()//2)
    toScreen(words2, font, colour, x, y+font.get_height()//2)

def toScreen3(words1, words2, words3, font, colour, x, y):
    toScreen(words1, font, colour, x, y-font.get_height())
    toScreen(words2, font, colour, x, y)
    toScreen(words3, font, colour, x, y+font.get_height())

def imageToScreen(imageName, x, y, width, height):
    image = pygame.image.load(imageName)
    image = pygame.transform.scale(image, (width, height))
    const.screen.blit(image, (x,y))

def isAllowedToMoveToDest(destinationPos):
    for x in const.BLOCKED_POSITIONS:
        if x[0] == destinationPos[0] and x[1] == destinationPos[1]:
            return False

    return True

def getActualGridSize():
    return const.GRID_SIZE * const.GRID_SCALING
