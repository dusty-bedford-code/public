import pygame as pg
from Images.ImageHolderTranslucent import ImageHolderTranslucent
from Constants import maxY

class Shadow(pg.sprite.Sprite):

    shadow_holder = ImageHolderTranslucent()

    def __init__(self, x, y, z, *group):
        super(Shadow, self).__init__(*group)

        self.x = x
        self.y = y
        self.z = z

        self.image = self.shadow_holder.get_image(self.x, self.y, int(self.z))
        self.rect = self.image.get_rect()


    def move(self, x, y, z):

        self.x = x
        self.y = y
        self.z = z

        #self.image = self.shadow_holder.get_image(self.x, self.y, int(self.z))

        self.image = self.shadow_holder.get_image(self.x, self.y, int(self.z)).copy()
        alpha1 = int(50 * (self.y / maxY(self.z)))
        #print(alpha1, self.y, maxY(self.z))
        self.image.set_alpha(alpha1 )
        #self.image.set_alpha(0 )
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = maxY(self.z) + 32
