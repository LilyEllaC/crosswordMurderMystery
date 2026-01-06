import pygame
import constants as const
import utility

# pylint: disable=no-member


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        image = pygame.image.load("assets/crow.png")

        self.image = pygame.transform.scale(image, (width, height))

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.movement = 1

        self.direction = "right"

    def set_direction(self, direction):
        if direction == self.direction:
            return

        self.direction = direction

        self.image = pygame.transform.flip(self.image, True, False)

    def toggle_direction(self):
        if self.direction == "right":
            self.direction = "left"
            self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.direction = "right"
            self.image = pygame.transform.flip(self.image, True, False)

    def draw(self):
        self.rect.x = self.x
        self.rect.y = self.y

        const.screen.blit(self.image, self.rect)


class Objects(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, appearance):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # image
        image = pygame.image.load(appearance)
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        self.rect.x = self.x
        self.rect.y = self.y

        const.screen.blit(self.image, self.rect)


class Button:
    def __init__(
        self, x, y, width, height, text, font, colour1, colour2, hasOutline: bool
    ):
        self.rect = None
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.text = text
        self.font = font

        self.colours = [colour1, colour2]
        self.colour = colour1
        self.textColour = const.BLUE

        self.hasOutline = hasOutline

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(const.screen, self.colour, self.rect)

        if self.hasOutline:
            pygame.draw.rect(const.screen, const.BLACK, self.rect, 3)
        if self.isHovered():
            self.colour=self.colours[1]
        else:
            self.colour=self.colours[0]
        
        utility.toScreen(
            self.text,
            self.font,
            self.textColour,
            self.x + self.width // 2,
            self.y + self.height // 2,
        )

    def isHovered(self):
        mouseX, mouseY = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouseX, mouseY):
            return True

        return False


# # sprites for different rooms #USELESS
# def spriteClues():
#     def __init__(self):
#         self.fryingPan = Objects(
#             const.WIDTH // 2, const.HEIGHT // 2, 50, 50, "fryingPan.png"
#         )
#         self.fruitBowl = Objects(
#             const.WIDTH // 2 + 100, const.HEIGHT // 2, 50, 50, "fruitBowl.png"
#         )
#         self.flowerPot = Objects(
#             const.WIDTH // 2 - 100, const.HEIGHT // 2, 50, 50, "flowerPot.png"
#         )
#         self.flowers = Objects(
#             const.WIDTH // 2 + 200, const.HEIGHT // 2, 50, 50, "flowers.png"
#         )
#         self.leadPipe = Objects(
#             const.WIDTH // 2 - 200, const.HEIGHT // 2, 50, 50, "pipe.png"
#         )
#         self.leadPipe = Objects(
#             const.WIDTH // 2 - 200, const.HEIGHT // 2, 50, 50, "pipe.png"
#         )
#         self.glasses = Objects(
#             const.WIDTH // 2 - 300, const.HEIGHT // 2, 50, 50, "glasses.png"
#         )
#         self.candle = Objects(
#             const.WIDTH // 2 + 300, const.HEIGHT // 2, 50, 50, "candleStick.png"
#         )
#         self.brokenMirror = Objects(
#             const.WIDTH // 2 - 400, const.HEIGHT // 2, 50, 50, "mirrorPieces.png"
#         )
#         self.wrench = Objects(
#             const.WIDTH // 2 + 400, const.HEIGHT // 2, 50, 50, "wrench.png"
#         )
#         self.rope = Objects(
#             const.WIDTH // 2, const.HEIGHT // 2 - 100, 50, 50, "rope.png"
#         )
#         self.clock = Objects(
#             const.WIDTH // 2, const.HEIGHT // 2 + 100, 50, 50, "brokenClock.png"
#         )

#         # creating sprite groups
#         self.kitchenSprites = pygame.sprite.Group()
#         self.bathroomSprites = pygame.sprite.Group()
#         self.livingRoomSprites = pygame.sprite.Group()
#         self.diningRoomSprites = pygame.sprite.Group()
#         self.bedroomSprites = pygame.sprite.Group()
#         self.gardenSprites = pygame.sprite.Group()
#         self.houseSprites = pygame.sprite.Group()

#         # adding
#         self.kitchenSprite.add(self.fryingPan, self.fruitBowl)
#         self.bathroomSprite.add(self.candleStick, self.brokenMirror)
#         self.livingRoomSprites.add(self.glasses)
#         self.diningRoomSprites.add(self.wrench, self.rope)
#         self.bedroomSprites.add(self.clock)
#         self.gardenSprites.add(self.flowerPot, self.flowers)
