import pygame
import intro
# pylint: disable=no-member
pygame.init()

import constants
import crossword

#running variable so it stops
running=True

#main
def main():
    global running

    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False


        intro.titleScreen()
        crossword.showCrossword()
        pygame.display.flip()

if __name__=="__main__":
    main()
    pygame.quit()