import pygame


import constants

pygame.init()
# pylint: disable=no-member

FONT_TYPE='w.ttf'
FONT15=pygame.font.Font(FONT_TYPE, 15)
FONT20=pygame.font.Font(FONT_TYPE, 20)
FONT25=pygame.font.Font(FONT_TYPE, 25)
FONT30=pygame.font.Font(FONT_TYPE, 30)
FONT37=pygame.font.Font(FONT_TYPE, 37)
FONT40=pygame.font.Font(FONT_TYPE, 40)
FONT200=pygame.font.Font(FONT_TYPE, 200)


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