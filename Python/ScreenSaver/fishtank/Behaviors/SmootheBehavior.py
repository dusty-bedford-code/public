from Behaviors import Behavior
import random
import math
import Constants
from Constants import maxY

class SmootheBehavior(Behavior.Behavior):

    def move(self):
        if self.duration == 0:

            angle = math.degrees(math.atan2(self.vy, self.vx))

            self.dvx = 0.0
            self.dvy = 0.0
            self.dvz = 0.0

            new_vx = self.vx
            new_vy = self.vy
            new_vz = self.vz

            # if angle between 0 and 180d don't flip, stan -x if -x, stay +x if +x

            x = random.randint(0, 20)
            if (x < 12):
                self.duration = random.randint(50, 50 + int(Constants.SCREEN_WIDTH / 6))
            elif(x < 18):
                self.duration = random.randint(20, 20 + int(Constants.SCREEN_WIDTH / 5))
            else:
                self.duration = random.randint(50, 50 + int(Constants.SCREEN_WIDTH / 4))

            old_sin_x = self.sign_x
            if (0 < angle < 180):
                self.sign_x = self.get_rand_sign_x()

            self.sign_y = self.get_rand_sign_y()

            self.sign_z = self.get_rand_sign_x()

            new_random = random.random()

            new_vx = new_random * self.sign_x * 4

            if (new_vx > 4.0):
                new_vx = 4.0

            angle_likely = random.randint(0,20)

            if angle_likely < 17:
                new_vy = (new_random / 1.5) * self.sign_y * 1
            else:
                new_vy = random.random() * self.sign_y * 2

            new_vz = (random.random() * self.sign_z) / 10

            if (self.sign_x == old_sin_x):
                self.dvx = (new_vx - self.vx) / self.duration
                self.dvy = (new_vy - self.vy) / self.duration
                self.dvz = (new_vz - self.vz) / self.duration
            else:
                self.dvx = (new_vx - self.vx) / 1
                self.dvy = (new_vy - self.vy) / 1
                self.vx += self.dvx
                self.vy += self.dvy
                self.dvx = 0.0
                self.dvy = 0.0
                self.dvz = (new_vz - self.vz) / self.duration

            #print("newvz:" + str(new_vz))

        if not (0 < self.z < 63):
            #print("Changing z" + str(self.z))
            self.vz = 0
            self.dvz *= -1
            self.sign_z *= -1
            new_vz = (random.random() * self.sign_z) / 10
            self.dvz = (new_vz - self.vz) / self.duration

        self.duration = self.duration - 1

        z_speed = ((60 + self.z) / 120.0) / 2

        self.vx += self.dvx
        self.vy += self.dvy
        self.vz += self.dvz

        self.x += self.vx * z_speed
        self.y += self.vy * z_speed
        self.z += self.vz * z_speed

        if self.z <= 0.0:
            self.sign_z *= -1
        elif self.z >= 63:
            self.sign_z *= -1

        cur_x = self.x
        cur_y = self.y
        cur_z = self.z


        if cur_y < self.min_y:
            self.y = self.min_y
            self.vy = 0.0
            self.dvy *= -1
            self.sign_y *= -1
        elif cur_y > maxY(cur_z):
            self.y = maxY(cur_z)
            self.sign_y *= -1

        if cur_x < self.min_x:
            self.x = self.min_x
            self.sign_x *= -1
            self.vx = 0.0
            self.dvx *= -1
        elif cur_x > self.max_x:
            self.x = self.max_x
            self.sign_x *= -1
            self.vx = 0.0
            self.dvx *= -1

        #if cur_z < 0:
        #    self.z = 0
        #elif cur_z > 64:
        #    cur_z = 64
