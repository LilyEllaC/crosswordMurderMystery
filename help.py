import constants as const
import sprites
import utility

backButton = sprites.Button(50, 0, 20, 80, "Back", const.FONT37, const.WHITE, const.BLACK, False)
backButton.textColour = const.BLACK

def showHelp():
    const.screen.fill(const.WHITE)
    backButton.draw()

    utility.toScreen3("1. Read all questions next to the Crossword",
                      "2. Search the clues in the house",
                      "3. Fill out the crossword to get the name of the murder",
                      const.FONT20, const.BLACK, const.WIDTH / 2, 100)

    utility.toScreen("Controls", const.FONT30, const.BLACK, const.WIDTH / 2, 180)
    utility.toScreen("W - Move forward", const.FONT20, const.BLACK, const.WIDTH / 2, 220)
    utility.toScreen("A - Move left", const.FONT20, const.BLACK, const.WIDTH / 2, 240)
    utility.toScreen("S - Move backwards", const.FONT20, const.BLACK, const.WIDTH / 2, 260)
    utility.toScreen("D - Move right", const.FONT20, const.BLACK, const.WIDTH / 2, 280)
    utility.toScreen("Move your mouse to click on buttons", const.FONT20, const.BLACK, const.WIDTH / 2, 300)

