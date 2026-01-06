import pygame
import utility
import constants as const
from sprites import Player
from sprites import Objects
from sprites import Button
pygame.init()

# pylint: disable=no-member

quitButton = Button(
    const.WIDTH / 10,
    const.HEIGHT - 300,
    100,
    50,
    "QUIT",
    const.FONT40,
    const.RED,
    const.DARK_RED,
    True,
)
startButton = Button(
    const.WIDTH / 10 - quitButton.width / 2,
    const.HEIGHT - 400,
    200,
    50,
    "START",
    const.FONT40,
    const.GREEN,
    const.DARK_GREEN,
    True,
)

helpButton=Button(10, const.HEIGHT - 50, 30, 45, "?", const.FONT37, const.LIGHT_RED, const.DARK_RED, False)
helpButton.textColour = const.BLACK

buttons = [startButton, quitButton, helpButton]


def titleScreen():
    bg = pygame.image.load("assets/start.png")
    bg = pygame.transform.scale(bg, (const.WIDTH, const.HEIGHT))

    const.screen.blit(bg, (0, 0))

    utility.toScreen(
        "Crossword Murder Mystery", const.FONT60, const.WHITE, const.WIDTH / 2, 80
    )

    # buttons
    for button in buttons:
        button.draw()

    # pylint: disable=no-member
