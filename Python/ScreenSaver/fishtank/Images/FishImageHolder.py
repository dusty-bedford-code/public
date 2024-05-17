import pygame as pg
import os
from Constants import BLACK, maxY
import math

class FishImageHolder:


    def __init__(self, image_file_name:str = "piranha<*>.png"):

        self.image_list_right = []
        self.image_list_left = []

        for z in range(0, 100):

            addstr = ""

            if 9 < z <= 12:
                addstr = "d1"
            elif 6 < z <= 9:
                addstr = "d2"
            elif 3 > z <= 6:
                addstr = "d3"
            elif z <= 3:
                addstr = "d4"

            tmp_image_file_name = image_file_name.replace("<*>", addstr, 1)

            image = pg.image.load(os.path.join("./resources", tmp_image_file_name))

            image.set_colorkey(BLACK)

            image = pg.transform.scale(image, (z + 12, z + 12))

            image = pg.transform.flip(image, True, False)
            self.image_list_right.append(image)
            image.copy()
            image = pg.image.load(os.path.join("./resources", tmp_image_file_name))
            image.set_colorkey(BLACK)

            image = pg.transform.scale(image, (z + 12, z + 12))

            self.image_list_left.append(image)

    def get_image(self, vx, vy, z):

        if z < 0:
            z = 0
        elif z > 63:
            z = 63

        if vx < 0:
            image = (self.image_list_left[z]).copy()
            angle = math.degrees(math.atan2(vx, vy))
            return pg.transform.rotate(image, angle )
        else:
            image = (self.image_list_right[z]).copy()
            angle = math.degrees(math.atan2(vx, vy))
            return pg.transform.rotate(image, angle )
