import constants as const
import sprites

backButton = sprites.Button(
    const.WIDTH / 10,
    const.HEIGHT - 300,
    100,
    50,
    "BACK TO MAIN MENU",
    const.FONT40,
    const.RED,
    const.DARK_RED,
    True,
)

def showEnd():
    const.screen.fill(const.WHITE)

    backButton.draw()
