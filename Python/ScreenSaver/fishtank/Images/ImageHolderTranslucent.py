import pygame as pg

from Constants import WHITE
import os

class ImageHolderTranslucent:

    image_list = []

    def __init__(self, shadow_file:str = "shadow.png"):

        image = pg.image.load(os.path.join("./resources", shadow_file))

        for z in range(0, 64):

            tmpImage = image.copy()

            tmpImage.set_colorkey(WHITE)
            tmpImage.set_alpha(50)
            tmpImage = pg.transform.scale(tmpImage, (z + 20, z + 20))

            self.image_list.append(tmpImage)

    def get_image(self, vx, vy, z):

        if (z < 0):
            z = 0
        if (z > 63):
            z = 63
        return self.image_list[z]

