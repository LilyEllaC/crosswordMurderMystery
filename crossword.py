import pygame
import constants as const
import utility
# pylint: disable=no-member

pygame.init()


def typing(event):
    #getting them to be allowed to type
    
    if event.key==pygame.K_BACKSPACE:
        letter=letter[:-1]
    else:
        letter+=event.unicode


class TextAndBoxes():
    def __init__(self):
        self.boxList=[]
        self.textList=[]
        #size=93
        gap=28.5
        width=0
        xPos=[]
        yPos=[]
        normalColour=0
        colour=3
        for i in range (0,20):
            xPos.append(11.5-width+27.6*i)
            yPos.append(26-width+29*i)


        #words
        #glasses
        self.textList.append(Letters("G", xPos[15], yPos[0]))
        self.boxList.append(Boxes(xPos[15], yPos[0], normalColour))
        self.textList.append(Letters("L", xPos[15], yPos[1]))
        self.boxList.append(Boxes(xPos[15], yPos[1], normalColour))
        self.textList.append(Letters("A", xPos[15], yPos[2]))
        self.boxList.append(Boxes(xPos[15], yPos[2], normalColour))
        self.textList.append(Letters("S", xPos[15], yPos[3]))
        self.boxList.append(Boxes(xPos[15], yPos[3], normalColour))
        self.textList.append(Letters("S", xPos[15], yPos[4]))
        self.boxList.append(Boxes(xPos[15], yPos[4], normalColour))
        self.textList.append(Letters("E", xPos[15], yPos[5]))
        self.boxList.append(Boxes(xPos[15], yPos[5], normalColour))
        self.textList.append(Letters("S", xPos[15], yPos[6]))
        self.boxList.append(Boxes(xPos[15], yPos[6], normalColour))
        #house
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
        #kitchen
        self.textList.append(Letters("K", xPos[11], yPos[7]))
        self.boxList.append(Boxes(xPos[11], yPos[7], normalColour))
        self.textList.append(Letters("I", xPos[11], yPos[8]))
        self.boxList.append(Boxes(xPos[11], yPos[8], normalColour))
        self.textList.append(Letters("T", xPos[11], yPos[9]))
        self.boxList.append(Boxes(xPos[11], yPos[9], normalColour))
        self.textList.append(Letters("C", xPos[11], yPos[10]))
        self.boxList.append(Boxes(xPos[11], yPos[10], normalColour))
        self.textList.append(Letters("H", xPos[11], yPos[11]))
        self.boxList.append(Boxes(xPos[11], yPos[11], normalColour))
        self.textList.append(Letters("E", xPos[11], yPos[12]))
        self.boxList.append(Boxes(xPos[11], yPos[12], normalColour))
        self.textList.append(Letters("N", xPos[11], yPos[13]))
        self.boxList.append(Boxes(xPos[11], yPos[13], normalColour))
        #cherry
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
        #blue
        self.textList.append(Letters("B", xPos[16], yPos[8]))
        self.boxList.append(Boxes(xPos[16], yPos[8], normalColour))
        self.textList.append(Letters("L", xPos[16], yPos[9]))
        self.boxList.append(Boxes(xPos[16], yPos[9], normalColour))
        self.textList.append(Letters("U", xPos[16], yPos[10]))
        self.boxList.append(Boxes(xPos[16], yPos[10], normalColour))
        self.textList.append(Letters("E", xPos[16], yPos[11]))
        self.boxList.append(Boxes(xPos[16], yPos[11], normalColour))
        #fryingpan
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
        #pipe
        self.textList.append(Letters("P", xPos[14], yPos[10]))
        self.boxList.append(Boxes(xPos[14], yPos[10], normalColour))
        self.textList.append(Letters("I", xPos[14], yPos[11]))
        self.boxList.append(Boxes(xPos[14], yPos[11], normalColour))
        self.textList.append(Letters("P", xPos[14], yPos[12]))
        self.boxList.append(Boxes(xPos[14], yPos[12], normalColour))
        self.textList.append(Letters("I", xPos[14], yPos[13]))
        self.boxList.append(Boxes(xPos[14], yPos[13], normalColour))
        #pink
        self.textList.append(Letters("P", xPos[19], yPos[10]))
        self.boxList.append(Boxes(xPos[19], yPos[10], normalColour))
        self.textList.append(Letters("I", xPos[19], yPos[11]))
        self.boxList.append(Boxes(xPos[19], yPos[11], normalColour))
        self.textList.append(Letters("N", xPos[19], yPos[12]))
        self.boxList.append(Boxes(xPos[19], yPos[12], normalColour))
        self.textList.append(Letters("K", xPos[19], yPos[13]))
        self.boxList.append(Boxes(xPos[19], yPos[13], normalColour))
        #mirror
        self.textList.append(Letters("M", xPos[1], yPos[13]))
        self.boxList.append(Boxes(xPos[1], yPos[13], normalColour))
        self.textList.append(Letters("I", xPos[1], yPos[14]))
        self.boxList.append(Boxes(xPos[1], yPos[14], normalColour))
        self.textList.append(Letters("R", xPos[1], yPos[15]))
        self.boxList.append(Boxes(xPos[1], yPos[15], normalColour))
        self.textList.append(Letters("R", xPos[1], yPos[16]))
        self.boxList.append(Boxes(xPos[1], yPos[16], normalColour))
        self.textList.append(Letters("O", xPos[1], yPos[17]))
        self.boxList.append(Boxes(xPos[1], yPos[17], normalColour))
        self.textList.append(Letters("R", xPos[1], yPos[18]))
        self.boxList.append(Boxes(xPos[1], yPos[18], normalColour))
        #apples
        self.textList.append(Letters("A", xPos[10], yPos[13]))
        self.boxList.append(Boxes(xPos[10], yPos[13], normalColour))
        self.textList.append(Letters("P", xPos[10], yPos[14]))
        self.boxList.append(Boxes(xPos[10], yPos[14], normalColour))
        self.textList.append(Letters("P", xPos[10], yPos[15]))
        self.boxList.append(Boxes(xPos[10], yPos[15], normalColour))
        self.textList.append(Letters("L", xPos[10], yPos[16]))
        self.boxList.append(Boxes(xPos[10], yPos[16], normalColour))
        self.textList.append(Letters("E", xPos[10], yPos[17]))
        self.boxList.append(Boxes(xPos[10], yPos[17], normalColour))
        self.textList.append(Letters("S", xPos[10], yPos[18]))
        self.boxList.append(Boxes(xPos[10], yPos[18], normalColour))
        
        #across words
        #flower
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
        #knife
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
        #fiveoclock
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
        self.boxList.append(Boxes(xPos[8], yPos[10], normalColour))
        self.textList.append(Letters("L", xPos[9], yPos[10]))
        self.boxList.append(Boxes(xPos[9], yPos[10], normalColour))
        self.textList.append(Letters("O", xPos[10], yPos[10]))
        self.boxList.append(Boxes(xPos[10], yPos[10], normalColour))
        self.textList.append(Letters("C", xPos[11], yPos[10]))
        self.boxList.append(Boxes(xPos[11], yPos[10], normalColour))
        self.textList.append(Letters("K", xPos[12], yPos[10]))
        self.boxList.append(Boxes(xPos[12], yPos[10], normalColour))
        #four
        self.textList.append(Letters("F", xPos[0], yPos[11]))
        self.boxList.append(Boxes(xPos[0], yPos[11], normalColour))
        self.textList.append(Letters("O", xPos[1], yPos[11]))
        self.boxList.append(Boxes(xPos[1], yPos[11], normalColour))
        self.textList.append(Letters("U", xPos[2], yPos[11]))
        self.boxList.append(Boxes(xPos[2], yPos[11], normalColour))
        self.textList.append(Letters("R", xPos[3], yPos[11]))
        self.boxList.append(Boxes(xPos[3], yPos[11], normalColour))
        #tiles
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
        #candlestick
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
        #rope
        self.textList.append(Letters("R", xPos[1], yPos[16]))
        self.boxList.append(Boxes(xPos[1], yPos[16], normalColour))
        self.textList.append(Letters("O", xPos[2], yPos[16]))
        self.boxList.append(Boxes(xPos[2], yPos[16], normalColour))
        self.textList.append(Letters("P", xPos[3], yPos[16]))
        self.boxList.append(Boxes(xPos[3], yPos[16], normalColour))
        self.textList.append(Letters("E", xPos[4], yPos[16]))
        self.boxList.append(Boxes(xPos[4], yPos[16], normalColour))
        #red
        self.textList.append(Letters("R", xPos[9], yPos[17]))
        self.boxList.append(Boxes(xPos[9], yPos[17], normalColour))
        self.textList.append(Letters("E", xPos[10], yPos[17]))
        self.boxList.append(Boxes(xPos[10], yPos[17], normalColour))
        self.textList.append(Letters("D", xPos[11], yPos[17]))
        self.boxList.append(Boxes(xPos[11], yPos[17], normalColour))
        #wrench
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
        self.boxList.append(Boxes(xPos[5], yPos[18], normalColour))
         

    def draw(self):
        for i in range(0, len(self.boxList)):
            self.boxList[i].hoveredOver()
            self.textList[i].draw()


class Boxes():
    def __init__(self, x, y, colourNum):
        self.x=x
        self.y=y
        self.colourNum=colourNum
        self.colours=[const.WHITE, const.GRAY, const.RED, const.DARK_RED]
        self.colour=self.colours[colourNum]
        self.rect=(x, y, 24.5, 27.5)
        self.image=pygame.draw.rect(const.screen, self.colour, self.rect)

    def hoveredOver(self):
        mouseX, mouseY=pygame.mouse.get_pos()
        #having it not flash
        if self.colourNum==0 or self.colourNum==1:
            self.colourNum=0
        else:
            self.colourNum=2
        #changing it
        if (mouseX>self.x and mouseX<self.x+28) and (mouseY>self.y and mouseY<self.y+28) and self.colourNum%2==0:
            self.colourNum+=1
                
        self.colour=self.colours[self.colourNum]
        self.image=pygame.draw.rect(const.screen, self.colour, self.rect)


class Letters():
    def __init__(self, correctLetter, x, y):
        self.letter=" "
        self.correctLetter=correctLetter
        self.x=x-14
        self.y=y-14

    def draw(self):
        if self.letter==self.correctLetter:
            colour=const.BLACK
        else: 
            colour=const.RED
        utility.toScreen(self.letter, const.FONT20, colour, self.x, self.y)


textAndBoxes=TextAndBoxes()
def showCrossword():
    #showing the crossword
    const.screen.fill(const.WHITE)
    utility.imageToScreen("crossword.png", 10, 25, 550, 550)
    utility.imageToScreen("across.png", 570, 25, 320, 240)
    utility.imageToScreen("downs.png", 570, 320, 325, 255)
    #drawBoxes(92, 315, const.RED)
    textAndBoxes.draw()

    