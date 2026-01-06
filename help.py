import constants as const
import sprites
import utility

backButton = sprites.Button(10, 0, 80, 80, "Back", const.FONT37, const.WHITE, const.BLACK, False)
backButton.textColour = const.BLACK

def showHelp():
    const.screen.fill(const.WHITE)
    backButton.draw()

    utility.toScreen("Goal", const.FONT30, const.BLACK, const.WIDTH / 2, 50)
    utility.toScreen3("1. Read all questions next to the Crossword",
                      "2. Search the clues in the house",
                      "3. Fill out the crossword to get the name of the murder",
                      const.FONT20, const.BLACK, const.WIDTH / 2, 110)

    utility.toScreen("Controls", const.FONT30, const.BLACK, const.WIDTH / 2, 180)
    utility.toScreen("W - Move forward", const.FONT20, const.BLACK, const.WIDTH / 2, 220)
    utility.toScreen("A - Move left", const.FONT20, const.BLACK, const.WIDTH / 2, 240)
    utility.toScreen("S - Move backwards", const.FONT20, const.BLACK, const.WIDTH / 2, 260)
    utility.toScreen("D - Move right", const.FONT20, const.BLACK, const.WIDTH / 2, 280)
    utility.toScreen("Move your mouse to click on buttons", const.FONT20, const.BLACK, const.WIDTH / 2, 300)

    utility.toScreen("Instructions for filling out the crossword: ", const.FONT30, const.BLACK, const.WIDTH / 2, 340)
    utility.toScreen2("Hold your mouse over the space you want to enter a letter in and click the letter", "If it is black it is correct, if it is red, it's wrong", const.FONT20, const.BLACK, const.WIDTH//2, 385)
    
    utility.toScreen("Helpful hints/tips", const.FONT30, const.BLACK, const.WIDTH / 2, 440)
    utility.toScreen2("The pink part of the painting is part of the foreground", "The person is holding something that you can also find elsewhere in the house", const.FONT20, const.BLACK, const.WIDTH//2, 490)
    utility.toScreen2("The bookshelf in question is beside the TV", "The object next to the sink is used for light", const.FONT20, const.BLACK, const.WIDTH//2, 535)

    

