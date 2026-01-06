import utility
import constants as const
import pygame
import game
import intro
import math
import time
import json

from enum import Enum

import utility

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

# DEV #####

leftCoords = []
rightCoords = []
topCoords = []
bottomCoords = []

###########


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

        # if ("w" in keysDown or "s" in keysDown) and (
        #     "d" in keysDown or "a" in keysDown
        # ):
        #     speed = speed / math.sqrt(2)

        if "w" in keysDown:
            newPos = (game.map.x, game.map.y + speed)

            if utility.isAllowedToMoveToDest(newPos):
                game.map.y += speed

        if "s" in keysDown:
            newPos = (game.map.x, game.map.y - speed)

            if utility.isAllowedToMoveToDest(newPos):
                game.map.y -= speed
        if "a" in keysDown:
            newPos = (game.map.x + speed, game.map.y)

            if utility.isAllowedToMoveToDest(newPos):
                game.map.x += speed

            game.player.set_direction("left")
        if "d" in keysDown:
            newPos = (game.map.x - speed, game.map.y)

            if utility.isAllowedToMoveToDest(newPos):
                game.map.x -= speed
            game.player.set_direction("right")


# main
def main():
    pygame.display.set_caption("Crossword Murder Mystery")

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

                if gameState == gameStates.PLAYING:
                    keys = pygame.key.get_pressed()

                    relative_x = (
                        game.player.x + game.player.width / 2 - 16
                    ) - game.map.x
                    relative_y = (
                        game.player.y + game.player.height / 2 - 16
                    ) - game.map.y

                    # map position

                    if keys[pygame.K_w]:
                        addKey("w")
                    if keys[pygame.K_s]:
                        addKey("s")
                    if keys[pygame.K_a]:
                        addKey("a")
                    if keys[pygame.K_d]:
                        addKey("d")
                    if keys[pygame.K_LEFT]:
                        if (relative_x, relative_y) in game.leftSquares:
                            game.leftSquares.remove((relative_x, relative_y))
                        else:
                            game.leftSquares.append((relative_x, relative_y))

                        if (game.map.x, game.map.y) in leftCoords:
                            leftCoords.remove((game.map.x, game.map.y))
                        else:
                            leftCoords.append((game.map.x, game.map.y))
                    if keys[pygame.K_RIGHT]:
                        if (relative_x, relative_y) in game.rightSquares:
                            game.rightSquares.remove((relative_x, relative_y))
                        else:
                            game.rightSquares.append((relative_x, relative_y))

                        if (game.map.x, game.map.y) in rightCoords:
                            rightCoords.remove((game.map.x, game.map.y))
                        else:
                            rightCoords.append((game.map.x, game.map.y))
                    if keys[pygame.K_UP]:
                        if (relative_x, relative_y) in game.topSquares:
                            game.topSquares.remove((relative_x, relative_y))
                        else:
                            game.topSquares.append((relative_x, relative_y))

                        if (game.map.x, game.map.y) in topCoords:
                            topCoords.remove((game.map.x, game.map.y))
                        else:
                            topCoords.append((game.map.x, game.map.y))
                    if keys[pygame.K_DOWN]:
                        if (relative_x, relative_y) in game.bottomSquares:
                            game.bottomSquares.remove((relative_x, relative_y))
                        else:
                            game.bottomSquares.append((relative_x, relative_y))

                        if (game.map.x, game.map.y) in bottomCoords:
                            bottomCoords.remove((game.map.x, game.map.y))
                        else:
                            bottomCoords.append((game.map.x, game.map.y))
                    if keys[pygame.K_p]:
                        with open("coords.json", "w") as f:
                            json.dump(
                                {
                                    "left": leftCoords,
                                    "right": rightCoords,
                                    "top": topCoords,
                                    "bottom": bottomCoords,
                                },
                                f,
                                indent=4,
                            )
                        print("SAVED TO FILE")

                if gameState == gameStates.CROSSWORD and event.type==pygame.KEYDOWN:
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
            crossword.showCrossword()
        elif gameState == gameStates.END:
            print("end")

        pygame.display.flip()


if __name__ == "__main__":
    main()
    pygame.quit()
