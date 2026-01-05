import pygame
import utility
import constants as const
from sprites import Player
from sprites import Objects
from sprites import Button
pygame.init()

# pylint: disable=no-member


startButton = Button(const.WIDTH // 2, const.HEIGHT - 150, 200, 50, "START", const.FONT40, const.GREEN,
                     const.DARK_GREEN, True)
quitButton = Button(const.WIDTH - 100, 50, 100, 50, "QUIT", const.FONT40, const.RED, const.DARK_RED, True)

buttons = [startButton, quitButton]


def titleScreen():
	bg = pygame.image.load("start.png")
	bg = pygame.transform.scale(bg, (const.WIDTH, const.HEIGHT))
	const.screen.blit(bg, (0, 0))

	# buttons
	for button in buttons:
		button.drawRect()

	# pylint: disable=no-member
