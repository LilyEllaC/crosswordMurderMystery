import pygame
import constants
import utility

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x=x
        self.y=y
        self.width=width
        self.height=height

        #image
        image=pygame.image.load("detective")
        self.image=pygame.transform.scale(image, (width, height))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

    def moving(self, xMove, yMove):
        self.x+=xMove
        self.y+=yMove


class Objects(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, appearance1, appearance2):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        
        #image
        image=pygame.image.load(appearance1)
        self.image1=appearance1
        self.image2=appearance2

        self.image=pygame.transform.scale(image, (width, height))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    
    def mouseOver(self):
        mouseX, mouseY=pygame.mouse.get_pos()
        if (mouseX>self.x and mouseX<self.x+self.width) and (mouseY>self.y and mouseY<self.y+self.height):
            self.image=pygame.transform.scale(pygame.image.load(self.image2), (self.width, self.height))
            return True
        else:
            return False
        

class Button():
    def __init__(self, x, y, width, height, text, font, colour1, colour2, hasOutline:bool):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.text=text
        self.font=font
        self.colours=[colour1, colour2]
        self.colour=colour1
        self.hasOutline=hasOutline

    def drawRect(self):
        rect=(self.x, self.y, self.width, self.height)
        pygame.draw.rect(constants.screen, self.colour, rect)
        if self.hasOutline:
            pygame.draw.rect(constants.screen, self.colour, rect, 3)
        utility.toScreen(self.text, self.font, self.x+self.width//2, self.y+self.height//2)


    def mouseHoveredOver(self):
        mouseX, mouseY=pygame.mouse.get_pos()
        if (mouseX>self.x and mouseX<self.x+self.width) and (mouseY>self.y and mouseY<self.y+self.height):
            self.colour=self.colours[1]
        else:
            self.colour=self.colours[0]
            

