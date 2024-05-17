MAX_DEPTH = 64
MAX_DEPTH_INDEX = MAX_DEPTH - 1

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255, 50)  # This color contains an extra integer. It's the alpha value.
PURPLE = (255, 0, 255)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_HEIGHT3RD = 600

def maxY(cur_z):
    return SCREEN_HEIGHT3RD + cur_z * 4.5
