import pygame

pygame.init()

import constants

# pylint: disable=no-member

#screen stuff (dimensions etc)
screen=pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("Crossword Game")
running=True


#helpful pushing text to screen function
def toScreen(words, font, colour, x, y):
    text=font.render(words, True, colour)
    textRect=text.get_rect()
    textRect.center=(x, y)
    screen.blit(text, textRect)
#versions to push more than 1 line
def toScreen2(words1, words2, font, colour, x, y):
    toScreen(words1, font, colour, x, y-font.get_height()//2)
    toScreen(words2, font, colour, x, y+font.get_height()//2)
def toScreen3(words1, words2, words3, font, colour, x, y):
    toScreen(words1, font, colour, x, y-font.get_height())
    toScreen(words2, font, colour, x, y)
    toScreen(words3, font, colour, x, y+font.get_height())



#main
def main():
    global running

    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

if __name__=="main":
    main()
    pygame.quit()