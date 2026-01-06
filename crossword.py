import pygame
import constants as const
import utility
from sprites import Button
# pylint: disable=no-member

pygame.init()

gameButton = Button(
    10, 10, 140, 50, "Game", const.FONT37, const.RED, const.DARK_RED, True
)


def isNumber(digit):
    for i in range(0, 10):
        if digit == str(i):
            return True

def drawOutline(x,y):
    rect=(x-1, y-1, 26, 29.5)
    pygame.draw.rect(const.screen, const.BLACK, rect, 3)


class TextAndBoxes:
    def __init__(self):
        self.boxList = []
        self.textList = []
        # size=93
        gap = 28.5
        width = 0
        xPos = []
        yPos = []
        normalColour = 0
        colour = 2
        for i in range(0, 20):
            xPos.append(11.5 - width + 27.6 * i)
            yPos.append(26 - width + 29 * i)

        # words
        # glasses
        if True:
            # glasses
            self.textList.append(Letters("G", xPos[15], yPos[0]))
            self.boxList.append(Boxes(xPos[15], yPos[0], normalColour))
            self.textList.append(Letters("L", xPos[15], yPos[1]))
            self.boxList.append(Boxes(xPos[15], yPos[1], normalColour))
            self.textList.append(Letters("A", xPos[15], yPos[2]))
            self.boxList.append(Boxes(xPos[15], yPos[2], normalColour))
            self.textList.append(Letters("S", xPos[15], yPos[3]))
            self.boxList.append(Boxes(xPos[15], yPos[3], colour))
            self.textList.append(Letters("S", xPos[15], yPos[4]))
            self.boxList.append(Boxes(xPos[15], yPos[4], normalColour))
            self.textList.append(Letters("E", xPos[15], yPos[5]))
            self.boxList.append(Boxes(xPos[15], yPos[5], normalColour))
            self.textList.append(Letters("S", xPos[15], yPos[6]))
            self.boxList.append(Boxes(xPos[15], yPos[6], normalColour))
            # house
            self.textList.append(Letters("H", xPos[13], yPos[4]))
            self.boxList.append(Boxes(xPos[13], yPos[4], normalColour))
            self.textList.append(Letters("O", xPos[13], yPos[5]))
            self.boxList.append(Boxes(xPos[13], yPos[5], normalColour))
            self.textList.append(Letters("U", xPos[13], yPos[6]))
            self.boxList.append(Boxes(xPos[13], yPos[6], normalColour))
            self.textList.append(Letters("S", xPos[13], yPos[7]))
            self.boxList.append(Boxes(xPos[13], yPos[7], normalColour))
            self.textList.append(Letters("E", xPos[13], yPos[8]))
            self.boxList.append(Boxes(xPos[13], yPos[8], normalColour))
            # kitchen
            self.textList.append(Letters("K", xPos[11], yPos[7]))
            self.boxList.append(Boxes(xPos[11], yPos[7], normalColour))
            self.textList.append(Letters("I", xPos[11], yPos[8]))
            self.boxList.append(Boxes(xPos[11], yPos[8], normalColour))
            self.textList.append(Letters("T", xPos[11], yPos[9]))
            self.boxList.append(Boxes(xPos[11], yPos[9], colour))
            self.textList.append(Letters("C", xPos[11], yPos[10]))
            self.boxList.append(Boxes(xPos[11], yPos[10], normalColour))
            self.textList.append(Letters("H", xPos[11], yPos[11]))
            self.boxList.append(Boxes(xPos[11], yPos[11], colour))
            self.textList.append(Letters("E", xPos[11], yPos[12]))
            self.boxList.append(Boxes(xPos[11], yPos[12], normalColour))
            self.textList.append(Letters("N", xPos[11], yPos[13]))
            self.boxList.append(Boxes(xPos[11], yPos[13], normalColour))
            # cherry
            self.textList.append(Letters("C", xPos[6], yPos[8]))
            self.boxList.append(Boxes(xPos[6], yPos[8], normalColour))
            self.textList.append(Letters("H", xPos[6], yPos[9]))
            self.boxList.append(Boxes(xPos[6], yPos[9], normalColour))
            self.textList.append(Letters("E", xPos[6], yPos[10]))
            self.boxList.append(Boxes(xPos[6], yPos[10], normalColour))
            self.textList.append(Letters("R", xPos[6], yPos[11]))
            self.boxList.append(Boxes(xPos[6], yPos[11], normalColour))
            self.textList.append(Letters("R", xPos[6], yPos[12]))
            self.boxList.append(Boxes(xPos[6], yPos[12], normalColour))
            self.textList.append(Letters("Y", xPos[6], yPos[13]))
            self.boxList.append(Boxes(xPos[6], yPos[13], normalColour))
            # blue
            self.textList.append(Letters("B", xPos[16], yPos[8]))
            self.boxList.append(Boxes(xPos[16], yPos[8], normalColour))
            self.textList.append(Letters("L", xPos[16], yPos[9]))
            self.boxList.append(Boxes(xPos[16], yPos[9], normalColour))
            self.textList.append(Letters("U", xPos[16], yPos[10]))
            self.boxList.append(Boxes(xPos[16], yPos[10], normalColour))
            self.textList.append(Letters("E", xPos[16], yPos[11]))
            self.boxList.append(Boxes(xPos[16], yPos[11], normalColour))
            # fryingpan
            self.textList.append(Letters("F", xPos[3], yPos[10]))
            self.boxList.append(Boxes(xPos[3], yPos[10], normalColour))
            self.textList.append(Letters("R", xPos[3], yPos[11]))
            self.boxList.append(Boxes(xPos[3], yPos[11], normalColour))
            self.textList.append(Letters("Y", xPos[3], yPos[12]))
            self.boxList.append(Boxes(xPos[3], yPos[12], normalColour))
            self.textList.append(Letters("I", xPos[3], yPos[13]))
            self.boxList.append(Boxes(xPos[3], yPos[13], normalColour))
            self.textList.append(Letters("N", xPos[3], yPos[14]))
            self.boxList.append(Boxes(xPos[3], yPos[14], normalColour))
            self.textList.append(Letters("G", xPos[3], yPos[15]))
            self.boxList.append(Boxes(xPos[3], yPos[15], normalColour))
            self.textList.append(Letters("P", xPos[3], yPos[16]))
            self.boxList.append(Boxes(xPos[3], yPos[16], normalColour))
            self.textList.append(Letters("A", xPos[3], yPos[17]))
            self.boxList.append(Boxes(xPos[3], yPos[17], normalColour))
            self.textList.append(Letters("N", xPos[3], yPos[18]))
            self.boxList.append(Boxes(xPos[3], yPos[18], normalColour))
            # pipe
            self.textList.append(Letters("P", xPos[14], yPos[10]))
            self.boxList.append(Boxes(xPos[14], yPos[10], normalColour))
            self.textList.append(Letters("I", xPos[14], yPos[11]))
            self.boxList.append(Boxes(xPos[14], yPos[11], normalColour))
            self.textList.append(Letters("P", xPos[14], yPos[12]))
            self.boxList.append(Boxes(xPos[14], yPos[12], colour))
            self.textList.append(Letters("E", xPos[14], yPos[13]))
            self.boxList.append(Boxes(xPos[14], yPos[13], normalColour))
            # pink
            self.textList.append(Letters("P", xPos[19], yPos[10]))
            self.boxList.append(Boxes(xPos[19], yPos[10], normalColour))
            self.textList.append(Letters("I", xPos[19], yPos[11]))
            self.boxList.append(Boxes(xPos[19], yPos[11], colour))
            self.textList.append(Letters("N", xPos[19], yPos[12]))
            self.boxList.append(Boxes(xPos[19], yPos[12], normalColour))
            self.textList.append(Letters("K", xPos[19], yPos[13]))
            self.boxList.append(Boxes(xPos[19], yPos[13], normalColour))
            # mirror
            self.textList.append(Letters("M", xPos[1], yPos[13]))
            self.boxList.append(Boxes(xPos[1], yPos[13], normalColour))
            self.textList.append(Letters("I", xPos[1], yPos[14]))
            self.boxList.append(Boxes(xPos[1], yPos[14], normalColour))
            self.textList.append(Letters("R", xPos[1], yPos[15]))
            self.boxList.append(Boxes(xPos[1], yPos[15], colour))
            self.textList.append(Letters("R", xPos[1], yPos[16]))
            self.boxList.append(Boxes(xPos[1], yPos[16], normalColour))
            self.textList.append(Letters("O", xPos[1], yPos[17]))
            self.boxList.append(Boxes(xPos[1], yPos[17], normalColour))
            self.textList.append(Letters("R", xPos[1], yPos[18]))
            self.boxList.append(Boxes(xPos[1], yPos[18], normalColour))
            # apples
            self.textList.append(Letters("A", xPos[10], yPos[13]))
            self.boxList.append(Boxes(xPos[10], yPos[13], normalColour))
            self.textList.append(Letters("P", xPos[10], yPos[14]))
            self.boxList.append(Boxes(xPos[10], yPos[14], normalColour))
            self.textList.append(Letters("P", xPos[10], yPos[15]))
            self.boxList.append(Boxes(xPos[10], yPos[15], normalColour))
            self.textList.append(Letters("L", xPos[10], yPos[16]))
            self.boxList.append(Boxes(xPos[10], yPos[16], normalColour))
            self.textList.append(Letters("E", xPos[10], yPos[17]))
            self.boxList.append(Boxes(xPos[10], yPos[17], colour))
            self.textList.append(Letters("S", xPos[10], yPos[18]))
            self.boxList.append(Boxes(xPos[10], yPos[18], normalColour))

            # across words
            # flower
            self.textList.append(Letters("F", xPos[11], yPos[5]))
            self.boxList.append(Boxes(xPos[11], yPos[5], normalColour))
            self.textList.append(Letters("L", xPos[12], yPos[5]))
            self.boxList.append(Boxes(xPos[12], yPos[5], normalColour))
            self.textList.append(Letters("O", xPos[13], yPos[5]))
            self.boxList.append(Boxes(xPos[13], yPos[5], normalColour))
            self.textList.append(Letters("W", xPos[14], yPos[5]))
            self.boxList.append(Boxes(xPos[14], yPos[5], normalColour))
            self.textList.append(Letters("E", xPos[15], yPos[5]))
            self.boxList.append(Boxes(xPos[15], yPos[5], normalColour))
            self.textList.append(Letters("R", xPos[16], yPos[5]))
            self.boxList.append(Boxes(xPos[16], yPos[5], normalColour))
            # knife
            self.textList.append(Letters("K", xPos[9], yPos[8]))
            self.boxList.append(Boxes(xPos[9], yPos[8], normalColour))
            self.textList.append(Letters("N", xPos[10], yPos[8]))
            self.boxList.append(Boxes(xPos[10], yPos[8], normalColour))
            self.textList.append(Letters("I", xPos[11], yPos[8]))
            self.boxList.append(Boxes(xPos[11], yPos[8], normalColour))
            self.textList.append(Letters("F", xPos[12], yPos[8]))
            self.boxList.append(Boxes(xPos[12], yPos[8], normalColour))
            self.textList.append(Letters("E", xPos[13], yPos[8]))
            self.boxList.append(Boxes(xPos[13], yPos[8], normalColour))
            # fiveoclock
            self.textList.append(Letters("F", xPos[3], yPos[10]))
            self.boxList.append(Boxes(xPos[3], yPos[10], normalColour))
            self.textList.append(Letters("I", xPos[4], yPos[10]))
            self.boxList.append(Boxes(xPos[4], yPos[10], normalColour))
            self.textList.append(Letters("V", xPos[5], yPos[10]))
            self.boxList.append(Boxes(xPos[5], yPos[10], normalColour))
            self.textList.append(Letters("E", xPos[6], yPos[10]))
            self.boxList.append(Boxes(xPos[6], yPos[10], normalColour))
            self.textList.append(Letters("O", xPos[7], yPos[10]))
            self.boxList.append(Boxes(xPos[7], yPos[10], normalColour))
            self.textList.append(Letters("C", xPos[8], yPos[10]))
            self.boxList.append(Boxes(xPos[8], yPos[10], colour))
            self.textList.append(Letters("L", xPos[9], yPos[10]))
            self.boxList.append(Boxes(xPos[9], yPos[10], normalColour))
            self.textList.append(Letters("O", xPos[10], yPos[10]))
            self.boxList.append(Boxes(xPos[10], yPos[10], normalColour))
            self.textList.append(Letters("C", xPos[11], yPos[10]))
            self.boxList.append(Boxes(xPos[11], yPos[10], normalColour))
            self.textList.append(Letters("K", xPos[12], yPos[10]))
            self.boxList.append(Boxes(xPos[12], yPos[10], normalColour))
            # four
            self.textList.append(Letters("F", xPos[0], yPos[11]))
            self.boxList.append(Boxes(xPos[0], yPos[11], normalColour))
            self.textList.append(Letters("O", xPos[1], yPos[11]))
            self.boxList.append(Boxes(xPos[1], yPos[11], normalColour))
            self.textList.append(Letters("U", xPos[2], yPos[11]))
            self.boxList.append(Boxes(xPos[2], yPos[11], normalColour))
            self.textList.append(Letters("R", xPos[3], yPos[11]))
            self.boxList.append(Boxes(xPos[3], yPos[11], colour))
            # tiles
            self.textList.append(Letters("T", xPos[13], yPos[11]))
            self.boxList.append(Boxes(xPos[13], yPos[11], normalColour))
            self.textList.append(Letters("I", xPos[14], yPos[11]))
            self.boxList.append(Boxes(xPos[14], yPos[11], normalColour))
            self.textList.append(Letters("L", xPos[15], yPos[11]))
            self.boxList.append(Boxes(xPos[15], yPos[11], normalColour))
            self.textList.append(Letters("E", xPos[16], yPos[11]))
            self.boxList.append(Boxes(xPos[16], yPos[11], normalColour))
            self.textList.append(Letters("S", xPos[17], yPos[11]))
            self.boxList.append(Boxes(xPos[17], yPos[11], normalColour))
            # candlestick
            self.textList.append(Letters("C", xPos[9], yPos[13]))
            self.boxList.append(Boxes(xPos[9], yPos[13], normalColour))
            self.textList.append(Letters("A", xPos[10], yPos[13]))
            self.boxList.append(Boxes(xPos[10], yPos[13], normalColour))
            self.textList.append(Letters("N", xPos[11], yPos[13]))
            self.boxList.append(Boxes(xPos[11], yPos[13], normalColour))
            self.textList.append(Letters("D", xPos[12], yPos[13]))
            self.boxList.append(Boxes(xPos[12], yPos[13], normalColour))
            self.textList.append(Letters("L", xPos[13], yPos[13]))
            self.boxList.append(Boxes(xPos[13], yPos[13], normalColour))
            self.textList.append(Letters("E", xPos[14], yPos[13]))
            self.boxList.append(Boxes(xPos[14], yPos[13], normalColour))
            self.textList.append(Letters("S", xPos[15], yPos[13]))
            self.boxList.append(Boxes(xPos[15], yPos[13], normalColour))
            self.textList.append(Letters("T", xPos[16], yPos[13]))
            self.boxList.append(Boxes(xPos[16], yPos[13], normalColour))
            self.textList.append(Letters("I", xPos[17], yPos[13]))
            self.boxList.append(Boxes(xPos[17], yPos[13], normalColour))
            self.textList.append(Letters("C", xPos[18], yPos[13]))
            self.boxList.append(Boxes(xPos[18], yPos[13], normalColour))
            self.textList.append(Letters("K", xPos[19], yPos[13]))
            self.boxList.append(Boxes(xPos[19], yPos[13], normalColour))
            # rope
            self.textList.append(Letters("R", xPos[1], yPos[16]))
            self.boxList.append(Boxes(xPos[1], yPos[16], normalColour))
            self.textList.append(Letters("O", xPos[2], yPos[16]))
            self.boxList.append(Boxes(xPos[2], yPos[16], colour))
            self.textList.append(Letters("P", xPos[3], yPos[16]))
            self.boxList.append(Boxes(xPos[3], yPos[16], normalColour))
            self.textList.append(Letters("E", xPos[4], yPos[16]))
            self.boxList.append(Boxes(xPos[4], yPos[16], normalColour))
            # red
            self.textList.append(Letters("R", xPos[9], yPos[17]))
            self.boxList.append(Boxes(xPos[9], yPos[17], normalColour))
            self.textList.append(Letters("E", xPos[10], yPos[17]))
            self.boxList.append(Boxes(xPos[10], yPos[17], normalColour))
            self.textList.append(Letters("D", xPos[11], yPos[17]))
            self.boxList.append(Boxes(xPos[11], yPos[17], normalColour))
            # wrench
            self.textList.append(Letters("W", xPos[0], yPos[18]))
            self.boxList.append(Boxes(xPos[0], yPos[18], normalColour))
            self.textList.append(Letters("R", xPos[1], yPos[18]))
            self.boxList.append(Boxes(xPos[1], yPos[18], normalColour))
            self.textList.append(Letters("E", xPos[2], yPos[18]))
            self.boxList.append(Boxes(xPos[2], yPos[18], normalColour))
            self.textList.append(Letters("N", xPos[3], yPos[18]))
            self.boxList.append(Boxes(xPos[3], yPos[18], normalColour))
            self.textList.append(Letters("C", xPos[4], yPos[18]))
            self.boxList.append(Boxes(xPos[4], yPos[18], normalColour))
            self.textList.append(Letters("H", xPos[5], yPos[18]))
            self.boxList.append(Boxes(xPos[5], yPos[18], colour))
        if True:
            #solution/murderer's name:
            yPosition=3
            self.yPosition=yPosition
            self.xPos=xPos
            self.yPos=yPos
            self.textList.append(Letters("C", xPos[0], yPos[yPosition]))
            self.boxList.append(Boxes(xPos[0], yPos[yPosition], normalColour))
            self.textList.append(Letters("H", xPos[1], yPos[yPosition]))
            self.boxList.append(Boxes(xPos[1], yPos[yPosition], normalColour))
            self.textList.append(Letters("R", xPos[2], yPos[yPosition]))
            self.boxList.append(Boxes(xPos[2], yPos[yPosition], normalColour))
            self.textList.append(Letters("I", xPos[3], yPos[yPosition]))
            self.boxList.append(Boxes(xPos[3], yPos[yPosition], normalColour))
            self.textList.append(Letters("S", xPos[4], yPos[yPosition]))
            self.boxList.append(Boxes(xPos[4], yPos[yPosition], normalColour))
            self.textList.append(Letters("T", xPos[5], yPos[yPosition]))
            self.boxList.append(Boxes(xPos[5], yPos[yPosition], normalColour))
            self.textList.append(Letters("O", xPos[6], yPos[yPosition]))
            self.boxList.append(Boxes(xPos[6], yPos[yPosition], normalColour))
            self.textList.append(Letters("P", xPos[7], yPos[yPosition]))
            self.boxList.append(Boxes(xPos[7], yPos[yPosition], normalColour))
            self.textList.append(Letters("H", xPos[8], yPos[yPosition]))
            self.boxList.append(Boxes(xPos[8], yPos[yPosition], normalColour))
            self.textList.append(Letters("E", xPos[9], yPos[yPosition]))
            self.boxList.append(Boxes(xPos[9], yPos[yPosition], normalColour))
            self.textList.append(Letters("R", xPos[10], yPos[yPosition]))
            self.boxList.append(Boxes(xPos[10], yPos[yPosition], normalColour))
            
            #numbers
            self.textList.append(Letters("3", xPos[11], yPos[5]))
            self.textList.append(Letters("6", xPos[9], yPos[8]))
            self.textList.append(Letters("11", xPos[0], yPos[11]))
            self.textList.append(Letters("12", xPos[13], yPos[11]))
            self.textList.append(Letters("14", xPos[9], yPos[13]))
            self.textList.append(Letters("16", xPos[1], yPos[16]))
            self.textList.append(Letters("17", xPos[9], yPos[17]))
            self.textList.append(Letters("18", xPos[0], yPos[18]))
            self.textList.append(Letters("1", xPos[15], yPos[0]))
            self.textList.append(Letters("2", xPos[13], yPos[4]))
            self.textList.append(Letters("4", xPos[11], yPos[7]))
            self.textList.append(Letters("5", xPos[6], yPos[8]))
            self.textList.append(Letters("7", xPos[16], yPos[8]))
            self.textList.append(Letters("8", xPos[3], yPos[10]))
            self.textList.append(Letters("9", xPos[14], yPos[10]))
            self.textList.append(Letters("10", xPos[19], yPos[10]))
            self.textList.append(Letters("13", xPos[1], yPos[13]))
            self.textList.append(Letters("15", xPos[10], yPos[13]))

            
            
    def outlines(self):
        drawOutline(self.xPos[0], self.yPos[self.yPosition])
        drawOutline(self.xPos[1], self.yPos[self.yPosition])
        drawOutline(self.xPos[2], self.yPos[self.yPosition])
        drawOutline(self.xPos[3], self.yPos[self.yPosition])
        drawOutline(self.xPos[4], self.yPos[self.yPosition])
        drawOutline(self.xPos[5], self.yPos[self.yPosition])
        drawOutline(self.xPos[6], self.yPos[self.yPosition])
        drawOutline(self.xPos[7], self.yPos[self.yPosition])
        drawOutline(self.xPos[8], self.yPos[self.yPosition])
        drawOutline(self.xPos[9], self.yPos[self.yPosition])
        drawOutline(self.xPos[10], self.yPos[self.yPosition])

    def draw(self):
        for i in range(0, len(self.boxList)):
            self.boxList[i].hoveredOver()
            self.textList[i].draw()
            if self.boxList[i].colourNum%2==1 and (i<len(self.boxList)-11 or self.checkIfCrosswordFinished()):
                self.textList[i].mouseOver=True
        
        #numbers
        for i in range(len(self.boxList), len(self.textList)):
            self.textList[i].draw()
            

    def checkIfCrosswordFinished(self):
        for i in range(0,len(self.textList)-29):
            if self.textList[i].letter!=self.textList[i].correctLetter:
                return False
        return True
    
    def checkIfNameCorrect(self):
        for i in range(len(self.textList)-29,len(self.textList)-18):
            if self.textList[i].letter!=self.textList[i].correctLetter:
                return False
        return True

    def showSpecial(self):
        for box in self.boxList:
            if box.special:
                box.colourNum = 2

    def resetLetters(self):
        for i in range(0, len(self.boxList)):
            self.textList[i].letter=" "
            self.boxList[i].colourNum=0


class Boxes:
    def __init__(self, x, y, colourNum):
        self.x = x
        self.y = y
        self.special = colourNum == 2

        self.colourNum = 0
        self.colours = [const.WHITE, const.GRAY, const.RED, const.DARK_RED]
        self.colour = self.colours[colourNum]
        self.rect = (x, y, 24, 27.5)
        self.image = pygame.draw.rect(const.screen, self.colour, self.rect)

    def hoveredOver(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        # having it not flash
        if self.colourNum == 0 or self.colourNum == 1:
            self.colourNum = 0
        else:
            self.colourNum = 2
        # changing it
        if (
            (mouseX > self.x and mouseX < self.x + 28)
            and (mouseY > self.y and mouseY < self.y + 28)
            and self.colourNum % 2 == 0
        ):
            self.colourNum += 1

        self.colour = self.colours[self.colourNum]
        self.image = pygame.draw.rect(const.screen, self.colour, self.rect)


class Letters:
    def __init__(self, correctLetter, x, y):
        self.letter = " "
        self.font = const.FONT20
        self.correctLetter = correctLetter
        self.x = x + 14
        self.y = y + 14
        if isNumber(correctLetter[0]):
            self.letter = correctLetter
            self.font = const.FONT10
            self.x = x + 3
            self.y = y + 3

        self.mouseOver = False

    def draw(self):
        self.mouseOver = False
        if self.letter == self.correctLetter:
            colour = const.BLACK
        else:
            colour = const.RED
        utility.toScreen(self.letter, self.font, colour, self.x, self.y)




def showQuestions():
    colour = const.BLACK
    font = const.FONT17
    y = 50
    gap = 20
    # acrosses
    if True:
        x = 570
        utility.toScreenTopLeft("Across", const.FONT25, colour, x, 20)
        utility.toScreenTopLeft(
            "3. What is in the victim's hand?", font, colour, x, y + gap * 0
        )  # flower
        utility.toScreenTopLeft(
            "6. What is on the island in the kitchen?", font, colour, x, y + gap * 1
        )
        utility.toScreenTopLeft(
            "8. What time is on the broken clock?", font, colour, x, y + gap * 2
        )
        utility.toScreenTopLeft(
            "11. How many flowers are in the pot?", font, colour, x, y + gap * 3
        )
        utility.toScreenTopLeft(
            "12. What is the floor of the bathroom made of?",
            font,
            colour,
            x,
            y + gap * 4,
        )
        utility.toScreenTopLeft(
            "14. What is on the edge of the sink?", font, colour, x, y + gap * 5
        )  # candle Stick
        utility.toScreenTopLeft(
            "16. What is hidden beside a chair?", font, colour, x, y + gap * 6
        )  # rope??
        utility.toScreenTopLeft(
            "17. What colour is the carpet in the hallways?",
            font,
            colour,
            x,
            y + gap * 7,
        )
        utility.toScreenTopLeft(
            "18. What tool is on the dining table?", font, colour, x, y + gap * 8
        )  # wrench

        # downs
        y = 345
        utility.toScreenTopLeft("Down", const.FONT25, colour, x, 315)
        utility.toScreenTopLeft(
            "1. What is under the desk?", font, colour, x, y + gap * 0
        )
        utility.toScreenTopLeft(
            "2. What is on the painting in the living room?",
            font,
            colour,
            x,
            y + gap * 1,
        )
        utility.toScreenTopLeft(
            "4. Which room has a window with red curtains?",
            font,
            colour,
            x,
            y + gap * 2,
        )  # kitchen
        utility.toScreenTopLeft(
            "5. What type of tree is on the painting in the",
            font,
            colour,
            x,
            y + gap * 3,
        )
        utility.toScreenTopLeft("   office?", font, colour, x, y + gap * 4)
        utility.toScreenTopLeft(
            "7. What colour is the leftmost book on the ", font, colour, x, y + gap * 5
        )
        utility.toScreenTopLeft(
            "   top shelf of the living room bookshelf?", font, colour, x, y + gap * 6
        )
        utility.toScreenTopLeft(
            "8. What is on the stove in the kitchen", font, colour, x, y + gap * 7
        )
        utility.toScreenTopLeft(
            "9. Source of the bathroom drip?", font, colour, x, y + gap * 8
        )  # pipe
        utility.toScreenTopLeft(
            "10. What colour are the flowers in the living room?",
            font,
            colour,
            x,
            y + gap * 9,
        )
        utility.toScreenTopLeft(
            "13. What is broken on the bathroom room?", font, colour, x, y + gap * 10
        )
        utility.toScreenTopLeft(
            "15. What fruit is in the bowl?", font, colour, x, y + gap * 11
        )  # apples


textAndBoxes = TextAndBoxes()

textAndBoxes=TextAndBoxes()
def showCrossword():
    # showing the crossword
    const.screen.fill(const.WHITE)
    utility.imageToScreen("crossword.png", 10, 25, 550, 550)
    showQuestions()
    textAndBoxes.draw()
    utility.toScreen2("When you have finished the crossword, unscramble the", "highlighted letters and enter the name you find here:", const.FONT15, const.BLACK, 170, 90)
    textAndBoxes.outlines()
    if textAndBoxes.checkIfCrosswordFinished():
        textAndBoxes.showSpecial()
    gameButton.draw()
    gameButton.isHovered()


def typing(event):
    # getting them to be allowed to type
    for text in textAndBoxes.textList:
        if text.mouseOver:
            if event.key == pygame.K_BACKSPACE:
                text.letter = " "
            elif text.letter == " ":
                text.letter = event.unicode.upper()
            text = text.letter
