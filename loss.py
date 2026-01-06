import constants as const
import sprites
import utility
import game
import datetime

backButton = sprites.Button(
    const.WIDTH//2,
    const.HEIGHT - 80,
    420,
    50,
    "BACK TO MAIN MENU",
    const.FONT40,
    const.RED,
    const.DARK_RED,
    True,
)

#having the crow
crow=sprites.Player(5, const.HEIGHT-200, 100, 50)

def showEnd():
    const.screen.fill(const.DARK_MAGENTA)
    utility.toScreen("You Died!", const.FONT200, const.BLACK, const.WIDTH//2, 110)
    utility.toScreen("The murderer caught you", const.FONT40, const.BLACK, const.WIDTH//2, 230)

    #moving the crow
    crow.draw()
    if crow.x<10:
        crow.movement=2
        crow.set_direction("right")
    elif crow.x>const.WIDTH-10-crow.width:
        crow.movement=-2
        crow.set_direction("left")
    crow.x+=crow.movement
    
    #button
    backButton.draw()


def resetVariables():
    game.startTime=None

