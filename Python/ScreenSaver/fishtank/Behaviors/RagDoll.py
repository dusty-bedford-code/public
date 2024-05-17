from Behaviors import Behavior
import math
import random
import Constants
from Constants import maxY

class RagDoll(Behavior.Behavior):

    def __init__(self, n):
        super(RagDoll, self).__init__(n)
        self.impulse = 0.0

    def move(self):

        if self.duration == 0:

            x = random.randint(0, 20)
            if (x < 12):
                self.duration = random.randint(50, 50 + int(Constants.SCREEN_WIDTH / 6))
            elif(x < 18):
                self.duration = random.randint(20, 20 + int(Constants.SCREEN_WIDTH / 5))
            else:
                self.duration = random.randint(50, 50 + int(Constants.SCREEN_WIDTH / 4))


            self.sign_x = self.get_rand_sign_x()
            self.sign_y = -1
            self.sign_z = self.get_rand_sign_x()

            new_random = random.random()


            axis = random.randint(0, 3)

            if axis == 0:
                self.dvx = new_random * self.sign_x
                self.vy = 0.0
                self.vz = 0.0
                self.impulse = random.randint(4, 12)
            elif axis == 1:
                self.vx = 0.0
                self.dvy = new_random * self.sign_y * 4
                self.vz = 0.0
            else:
                self.vx = 0.0
                self.vy = 0.0
                self.vz = 0.0


        self.duration = self.duration - 1

        z_speed = ((60 + self.z) / 120.0) / 2

        self.impulse -= 1
        if self.impulse > 0:
            self.vy += self.dvy

        self.x += self.vx * z_speed
        self.y += self.vy * z_speed
        self.z += self.vz * z_speed

        self.vy += .40
        if (self.vy > 4.0):
            self.vy = 4.0

        if not (0 < self.z <= 63):
            self.vz *= -1
            if (self.z < 0):
                self.z = 0
            elif(self.z > 63):
                self.z = 63

        if not(self.min_y <= self.y < maxY(self.z)):
            self.vy = 0.0
            if (self.y < self.min_y):
                self.y = self.min_y
                self.impulse = 0.0
            elif(self.y > maxY(self.z)):
                self.y = maxY(self.z)
                self.impulse = 0.0

        if not(self.min_x < self.x < self.max_x):
            self.vx *= -1
            if (self.x < self.min_x):
                self.x = self.min_x
            elif(self.x > self.max_x):
                self.x = self.max_x

