#helpful pushing text to screen function
def toScreen(words, font, colour, x, y, screen):
    text=font.render(words, True, colour)
    textRect=text.get_rect()
    textRect.center=(x, y)
    screen.blit(text, textRect)

#versions to push more than 1 line
def toScreen2(words1, words2, font, colour, x, y, screen):
    toScreen(words1, font, colour, x, y-font.get_height()//2, screen)
    toScreen(words2, font, colour, x, y+font.get_height()//2, screen)

def toScreen3(words1, words2, words3, font, colour, x, y, screen):
    toScreen(words1, font, colour, x, y-font.get_height(), screen)
    toScreen(words2, font, colour, x, y, screen)
    toScreen(words3, font, colour, x, y+font.get_height(), screen)