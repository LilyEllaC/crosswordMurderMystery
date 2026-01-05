import pygame
import constants as const
import utility
pygame.init()

def showCrossword():
    #showing the crossword
    const.screen.fill(const.WHITE)
    utility.imageToScreen("crossword.png", 10, 25, 550, 550)
    utility.imageToScreen("across.png", 570, 25, 320, 240)
    utility.imageToScreen("downs.png", 570, 320, 325, 255)
    #drawBoxes(92, 315, const.RED)


def typing():
    #getting them to be allowed to type
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN():
            if event.key==pygame.K_BACKSPACE:
                letter=letter[:-1]
            else:
                letter+=event.unicode


class TextAndBoxes():
    def __init__(self):
        self.boxList=[]
        self.textList=[]
        #size=93
        gap=28
        width=0
        xPos=[]
        yPos=[]
        normalColour=2
        colour=3
        for i in range (0,20):
            xPos.append(10-width+gap*i)
            yPos.append(25-width+gap*i)


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
        #pipe
        self.textList.append(Letters("B", xPos[16], yPos[8]))
        self.boxList.append(Boxes(xPos[16], yPos[8], normalColour))
        




class Boxes():
    def __init__(self, x, y, colourNum):
        self.x=x
        self.y=y
        self.colourNum=colourNum
        self.colours=[const.WHITE, const.GRAY, const.RED, const.DARK_RED]
        self.colour=self.colours[colourNum]
        rect=(x, y, 28, 28)
        self.image=pygame.draw.rect(const.screen, self.colour, rect)

    def hoveredOver(self):
        mouseX, mouseY=pygame.mouse.get_pos()
        if (mouseX>self.x and mouseX<self.x+28) and (mouseY>self.y and mouseY<self.y+28) and self.colourNum%2!=0:
            self.colourNum+=1
        elif self.colourNum%0==0:
            self.colourNum-=1
        
        self.colour=self.colours[self.colourNum]


class Letters():
    def __init__(self, correctLetter, x, y):
        self.letter=" "
        self.correctLetter=correctLetter
        self.x=x
        self.y=y

    def draw(self):
        if self.letter==self.correctLetter:
            colour=const.BLACK
        else: 
            colour=const.RED
        utility.toScreen(self.letter, const.FONT20, colour, self.x, self.y)





    