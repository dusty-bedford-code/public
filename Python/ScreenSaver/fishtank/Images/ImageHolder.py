class ShadowImageHolder:

    image_list = []

    def __init__(self, filename, colorkey):

        self.depth = 1

        if (len(image_list) == 0):

            for z in range(0, MAX_DEPTH):

                image = pg.image.load(os.path.join("resources", filename))

                image.set_colorkey(colorkey)
                image.set_alpha(50)

                image = pg.transform.scale(image, (z + 20, z + 20))

                self.image_list.append(image)


    def get_image(self, vx, vy, z):

        if (z < 0):
            z = 0
        if (z > MAX_DEPTH_INDEX):
            z = MAX_DEPTH_INDEX

        return self.image_list[z]
