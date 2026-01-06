import constants as const
import sprites
import utility

backButton = sprites.Button(10, 0, 80, 80, "Back", const.FONT37, const.WHITE, const.BLACK, False)
backButton.textColour = const.BLACK

def showHelp():
    const.screen.fill(const.WHITE)
    backButton.draw()

    utility.toScreen("Goal", const.FONT30, const.BLACK, const.WIDTH / 2, 100)
    utility.toScreen3("1. Read all questions next to the Crossword",
                      "2. Search the clues in the house",
                      "3. Fill out the crossword to get the name of the murder",
                      const.FONT20, const.BLACK, const.WIDTH / 2, 160)

    utility.toScreen("Controls", const.FONT30, const.BLACK, const.WIDTH / 2, 240)
    utility.toScreen("W - Move forward", const.FONT20, const.BLACK, const.WIDTH / 2, 280)
    utility.toScreen("A - Move left", const.FONT20, const.BLACK, const.WIDTH / 2, 300)
    utility.toScreen("S - Move backwards", const.FONT20, const.BLACK, const.WIDTH / 2, 320)
    utility.toScreen("D - Move right", const.FONT20, const.BLACK, const.WIDTH / 2, 340)
    utility.toScreen("Move your mouse to click on buttons", const.FONT20, const.BLACK, const.WIDTH / 2, 360)

