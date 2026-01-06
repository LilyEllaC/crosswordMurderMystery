import sys
import datetime
import constants as const
import pygame
import game
import help
import intro
import end
import asyncio

# import math
import time
import json

from enum import Enum

import utility

# pylint: disable=no-member

pygame.init()
import crossword

# running variable so it stops
running = True
clock = pygame.time.Clock()


class gameStates(Enum):
    STARTING_SCREEN = 1
    PLAYING = 2
    CROSSWORD = 3
    END = 4
    HELP = 5


keysDown = []

lastMoveTS = 0
moveDelay = 150

# DEV #####

existingCoords = const.existingCoords

# {
#     "left/right/top/bottom": [
#         [
#             {
#                 "relative": [
#                     X,
#                     Y
#                 ],
#                 "absolute": [
#                     X,
#                     Y
#                 ]
#             }
#         ]
#     ],
# }

leftCoords = existingCoords["left"]
rightCoords = existingCoords["right"]
topCoords = existingCoords["top"]
bottomCoords = existingCoords["bottom"]

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
            # newPos = (game.map.x, game.map.y + speed)

            if utility.isAllowedToMoveToDest("top"):
                game.map.y += speed

        if "s" in keysDown:
            # newPos = (game.map.x, game.map.y - speed)

            if utility.isAllowedToMoveToDest("bottom"):
                game.map.y -= speed
        if "a" in keysDown:
            # newPos = (game.map.x + speed, game.map.y)

            if utility.isAllowedToMoveToDest("left"):
                game.map.x += speed

            game.player.set_direction("left")
        if "d" in keysDown:
            # newPos = (game.map.x - speed, game.map.y)

            if utility.isAllowedToMoveToDest("right"):
                game.map.x -= speed
            game.player.set_direction("right")


def addToSquare():
    if not const.DEV_MODE:
        return

    game.leftSquares = []
    game.rightSquares = []
    game.topSquares = []
    game.bottomSquares = []

    for coord in leftCoords:
        game.leftSquares.append(coord["relative"])
    for coord in rightCoords:
        game.rightSquares.append(coord["relative"])
    for coord in topCoords:
        game.topSquares.append(coord["relative"])
    for coord in bottomCoords:
        game.bottomSquares.append(coord["relative"])


# main
async def main():
    pygame.display.set_caption("Crossword Murder Mystery")

    global running

    gameState = gameStates.STARTING_SCREEN

    addToSquare()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == const.GAME_ENDED_EVENT:
                gameState = gameStates.END

            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                if gameState == gameStates.STARTING_SCREEN:
                    if intro.startButton.isHovered():
                        gameState = gameStates.PLAYING
                        game.startTime = datetime.datetime.now()
                    elif intro.quitButton.isHovered():
                        running = False

                if gameState == gameStates.END:
                    if end.backButton.isHovered():
                        gameState = gameStates.STARTING_SCREEN

                if gameState == gameStates.PLAYING:
                    if (
                        game.crosswordButton.isHovered()
                        and event.type == pygame.MOUSEBUTTONDOWN
                    ):
                        gameState = gameStates.CROSSWORD
                        continue

                    if game.helpButton.isHovered() and event.type==pygame.MOUSEBUTTONDOWN:
                        gameState=gameStates.HELP
                        continue

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
                        if const.DEV_MODE:
                            if utility.checkCoords(leftCoords):
                                idx = utility.findCoordIndex(leftCoords)
                                leftCoords.pop(idx)
                            else:
                                leftCoords.append(
                                    {
                                        "relative": [relative_x, relative_y],
                                        "absolute": [game.map.x, game.map.y],
                                    }
                                )

                    if keys[pygame.K_RIGHT]:
                        if const.DEV_MODE:
                            if utility.checkCoords(rightCoords):
                                idx = utility.findCoordIndex(rightCoords)
                                rightCoords.pop(idx)
                            else:
                                rightCoords.append(
                                    {
                                        "relative": [relative_x, relative_y],
                                        "absolute": [game.map.x, game.map.y],
                                    }
                                )

                    if keys[pygame.K_UP]:
                        if const.DEV_MODE:
                            if utility.checkCoords(topCoords):
                                idx = utility.findCoordIndex(topCoords)
                                topCoords.pop(idx)
                            else:
                                topCoords.append(
                                    {
                                        "relative": [relative_x, relative_y],
                                        "absolute": [game.map.x, game.map.y],
                                    }
                                )

                    if keys[pygame.K_DOWN]:
                        if const.DEV_MODE:
                            if utility.checkCoords(bottomCoords):
                                idx = utility.findCoordIndex(bottomCoords)
                                bottomCoords.pop(idx)
                            else:
                                bottomCoords.append(
                                    {
                                        "relative": [relative_x, relative_y],
                                        "absolute": [game.map.x, game.map.y],
                                    }
                                )
                    if keys[pygame.K_r]:
                        if const.DEV_MODE:
                            const.reevalConstants(
                                {
                                    "left": leftCoords,
                                    "right": rightCoords,
                                    "top": topCoords,
                                    "bottom": bottomCoords,
                                }
                            )
                    if keys[pygame.K_p]:
                        if const.DEV_MODE and sys.platform != "emscripten":
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
                    if keys[pygame.K_t]:
                        game.player.toggle_direction()

                    addToSquare()

                if gameState == gameStates.CROSSWORD:
                    if event.type == pygame.KEYDOWN:
                        crossword.typing(event)
                    if (
                        event.type == pygame.MOUSEBUTTONDOWN
                        and crossword.gameButton.isHovered
                    ):
                        gameState = gameStates.PLAYING

                if gameState == gameStates.HELP:
                    if event.type == pygame.MOUSEBUTTONDOWN and help.backButton.isHovered():
                        gameState=gameStates.PLAYING

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
            game.showGame()
        elif gameState == gameStates.CROSSWORD:
            crossword.showCrossword()
        elif gameState == gameStates.END:
            end.showEnd()
        elif gameState == gameStates.HELP:
            help.showHelp()

        pygame.display.flip()
        clock.tick(const.FPS)
        await asyncio.sleep(0)


if __name__ == "__main__":
    asyncio.run(main())
    pygame.quit()
