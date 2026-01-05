import pygame
import intro

pygame.init()

import constants
# pylint: disable=no-member

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
        pygame.display.flip()

if __name__=="__main__":
    main()
    pygame.quit()