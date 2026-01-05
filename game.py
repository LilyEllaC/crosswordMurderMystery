import constants as const
from sprites import Objects, Player

map = Objects(0, 0, 992, 736, "assets/map.png")
player = Player(20, 20, 20, 20)

def show_game():
    const.screen.fill(const.BLACK)

    map.draw()
    player.draw()