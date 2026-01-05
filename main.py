import pygame

pygame.init()

import constants
# pylint: disable=no-member

#screen stuff (dimensions etc)
screen=pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("Crossword Game")
running=True

#main
def main():
    global running

    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

        bg = pygame.image.load("start.png")
        bg = pygame.transform.scale(bg, (constants.WIDTH, constants.HEIGHT))
        screen.blit(bg, (0,0))
        pygame.display.flip()

if __name__=="__main__":
    main()
    pygame.quit()