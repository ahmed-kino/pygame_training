TITLE = 'Jumpy!'

#Basic settings
BLACK  = (0, 0, 0)
WHITE  = (255,255,255)
RED    = (255, 0, 0)
BLUE  = (0, 0, 255)
GREEN   = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CHAIN  = (0, 255, 255)

SIZE = WIDTH, HEIGHT = 800, 600
FPS = 60


# Platform settings
PLATFORM_LIST = [(0, HEIGHT - 30),
                 (40, HEIGHT - 150),
                 (50, HEIGHT - 550),
                 (300, HEIGHT - 250),
                 (0, HEIGHT - 350),]
# Player settings
PLAYER_ACC = 1.5
PLAYER_FRICTION = -0.2
PLAYER_JUMP = 300
GRAVITY = 1

SKY_COLOUR_RANGE = [
    (102, 204, 255),
    (26, 178, 255),
    (0, 153, 230),
    (128, 128, 255),
    (102, 102, 255),
    (102, 26, 255),
    (204, 102, 255),
    (255, 0, 102),
    (255, 102, 102),
    (255, 51, 51),
    (255, 0, 0),
    (230, 0, 0),
    (153, 0, 77),
    (128, 0, 64),
    (0, 0, 128),
    (0, 0, 102),
    (0, 0, 77),
    (0, 0, 51),
    (0, 0, 26),
    (1, 1, 1)
]