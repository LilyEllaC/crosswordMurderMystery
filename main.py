import pygame
import game
import intro
import math
import time

from enum import Enum
# pylint: disable=no-member

pygame.init()
import crossword

# running variable so it stops
running = True


class gameStates(Enum):
    STARTING_SCREEN = 1
    PLAYING = 2
    CROSSWORD = 3
    END = 4


keysDown = []

lastMoveTS = 0
moveDelay = 150


def addKey(key):
    if key not in keysDown:
        keysDown.append(key)


def removeKey(key):
    if key in keysDown:
        keysDown.remove(key)


def move(bypassDebounce):
    global lastMoveTS

    time_ms = time.time_ns() // 1_000_000

    if bypassDebounce or time_ms - lastMoveTS > moveDelay:
        lastMoveTS = time_ms

        speed = 32

        if ("w" in keysDown or "s" in keysDown) and (
            "d" in keysDown or "a" in keysDown
        ):
            speed = speed / math.sqrt(2)

        if "w" in keysDown:
            game.map.y += speed
        if "s" in keysDown:
            game.map.y -= speed
        if "a" in keysDown:
            game.map.x += speed
            game.player.set_direction("left")
        if "d" in keysDown:
            game.map.x -= speed
            game.player.set_direction("right")


# main
def main():
    pygame.display.set_caption("Crossword Game")

    global running

    gameState = gameStates.STARTING_SCREEN

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                if gameState == gameStates.STARTING_SCREEN:
                    if intro.startButton.isHovered():
                        gameState = gameStates.PLAYING
                    elif intro.quitButton.isHovered():
                        running = False

                if (
                    gameState == gameStates.PLAYING
                ):
                    keys = pygame.key.get_pressed()

                    if keys[pygame.K_w]:
                        addKey("w")
                    if keys[pygame.K_s]:
                        addKey("s")
                    if keys[pygame.K_a]:
                        addKey("a")
                    if keys[pygame.K_d]:
                        addKey("d")
                if gameState==gameStates.CROSSWORD:
                    crossword.typing(event)
                move(True)

            elif event.type == pygame.KEYUP:
                keys = pygame.key.get_pressed()

                if not keys[pygame.K_w]:
                    removeKey("w")
                if not keys[pygame.K_s]:
                    removeKey("s")
                if not keys[pygame.K_a]:
                    removeKey("a")
                if not keys[pygame.K_d]:
                    removeKey("d")

        move(False)

        if gameState == gameStates.STARTING_SCREEN:
            intro.titleScreen()
        elif gameState == gameStates.PLAYING:
            game.show_game()
        elif gameState == gameStates.CROSSWORD:
            print("playing with crossword open")
        elif gameState == gameStates.END:
            print("end")

        pygame.display.flip()


if __name__ == "__main__":
    main()
    pygame.quit()
