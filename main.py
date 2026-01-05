import pygame

import game
import intro
from enum import Enum

pygame.init()

import constants
# pylint: disable=no-member

#running variable so it stops
running=True

class gameStates(Enum):
    STARTING_SCREEN = 1
    PLAYING = 2
    PLAYING_WITH_CROSSWORD_OPEN = 3
    END = 4

#main
def main():
    pygame.display.set_caption("Crossword Game")
    global running
    gameState=gameStates.STARTING_SCREEN

    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if intro.startButton.rect.collidepoint(event.pos):
                    gameState=gameStates.PLAYING
                elif intro.quitButton.rect.collidepoint(event.pos):
                    running=False

        if gameState == gameStates.STARTING_SCREEN:
            intro.titleScreen()
        elif gameState == gameStates.PLAYING:
            game.show_game()
        elif gameState == gameStates.PLAYING_WITH_CROSSWORD_OPEN:
            print("playing with crossword open")
        elif gameState == gameStates.END:
            print("end")

        pygame.display.flip()

if __name__=="__main__":
    main()
    pygame.quit()