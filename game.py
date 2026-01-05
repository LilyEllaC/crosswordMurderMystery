import constants as const
from sprites import Objects, Player

map = Objects(0, 0, 992 * 2, 736 * 2, "assets/map.png")
player = Player(const.WIDTH / 2, const.HEIGHT / 2, 39, 35)

def show_game():
    const.screen.fill(const.BLACK)

    map.draw()
    player.draw()