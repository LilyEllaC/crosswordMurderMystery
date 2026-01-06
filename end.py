import constants as const
import sprites
import utility

backButton = sprites.Button(
    const.WIDTH // 2,
    const.HEIGHT - 80,
    420,
    50,
    "BACK TO MAIN MENU",
    const.FONT40,
    const.RED,
    const.DARK_RED,
    True,
)

# having the crow
crow = sprites.Player(5, const.HEIGHT - 200, 50, 100)


def showEnd():
    const.screen.fill(const.DARK_MAGENTA)
    utility.toScreen2(
        "Congratulations!",
        "You caught the murderer.",
        const.FONT40,
        const.BLACK,
        const.WIDTH // 2,
        100,
    )

    # moving the crow
    crow.draw()
    if crow.x < 10:
        crow.movement = 5
        crow.set_direction("right")
    elif crow.x > const.WIDTH - 10 - crow.width:
        crow.movement = -5
        crow.set_direction("left")
    crow.x += crow.movement

    # button
    backButton.draw()
