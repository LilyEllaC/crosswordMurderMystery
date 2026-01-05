import pygame

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


class objects(pygame.sprite.Sprite):
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
        