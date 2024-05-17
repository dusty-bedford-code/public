import pygame as pg
import Constants
from Constants import maxY
from Behaviors.Behavior import Behavior

class Fish(pg.sprite.Sprite):

    def __init__(self, index, pos, shadow, image_holder, group, behavior: [Behavior] = Behavior()) -> None:

        self.behavior = behavior

        super(Fish, self).__init__(group)

        self.group = group
        self.image_holder = image_holder
        self.index = index
        self.shadow = shadow

        self.behavior.setMaxX(Constants.SCREEN_WIDTH + 100)
        self.behavior.setMaxY(Constants.SCREEN_HEIGHT + 100)
        self.behavior.setInitialValues(pos)

        (x, y, z, vx, vy, vz) = self.behavior.getState()

        self.shadow.x = x
        self.shadow.y = maxY(z)
        self.shadow.move(x, y, z)

        self.image = self.image_holder.get_image(vx, vy, z)

        self.rect = self.image.get_rect()

    def setPos(self, x, y , z):
        self.behavior.x = x
        self.behavior.y = y
        self.behavior.z = z

    def move(self):

        self.behavior.move()

        (x, y, z, vx, vy, vz) = self.behavior.getState()

        self.image = self.image_holder.get_image(vx, vy, int(z))

        self.shadow.x = x
        self.shadow.y = maxY(z)
        self.shadow.z = z
        self.shadow.move(x, y, z)
        self.group.change_layer(self, (int(z) * 1000) + self.index)

        self.rect.x = x
        self.rect.y = y

