import pygame

# pylint: disable=no-member

pygame.init()

#screen stuff (dimensions etc)
WIDTH, HEIGHT=900,600
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crossword Game")
running=True

#code
clock=pygame.time.Clock()
FPS=30
FPSScaling=30/FPS



#main
def main():
    global running

    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False

if __name__=="main":
    main()
    pygame.quit()