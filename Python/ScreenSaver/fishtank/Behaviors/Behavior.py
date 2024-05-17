import random
import Constants
from Constants import maxY

class Behavior:

    def setMaxX(self, x):
        self.max_x = x

    def setMaxY(self, y):
        self.max_y = y

    def setMinY(self, y):
        self.min_y = y

    def __init__(self, index: int = 0) -> None:
        super(Behavior, self).__init__()
        self.duration = 0
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.layer = 0
        self.vx = 0.0
        self.vy = 0.0
        self.vz = 0.0
        self.dvx = 0.0
        self.dvy = 0.0
        self.dvz = 0.0
        self.sign_x = 1
        self.sign_y = 1
        self.sign_z = 1
        self.min_x = -100
        self.min_y = -100
        self.max_x = 0
        self.max_y = 0
        self.index = index
        self.negative_y = 10

    def setInitialValues(self, pos):

        self.z = random.randint(1,64)
        self._layer = int((self.z * 1000) + self.index)

        self.vx = random.random() / 10 + .1
        self.vy = random.random() / 10 + .1
        self.vz = random.random() / 10 + .1
        self.dvx = 0.0
        self.dvy = 0.0
        self.dvz = 0.0

        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]

        self.max_x = Constants.SCREEN_WIDTH + 100
        self.max_y = Constants.SCREEN_HEIGHT + 100
        self.angle_inc = 0

    def getState(self) -> (float, float, float, float, float, float):
        return (self.x, self.y, self.z, self.vx, self.vy, self.vz)

    def move(self):
        if self.duration == 0:

            x = random.randint(0, 20)
            if (x < 12):
                self.duration = random.randint(5, int(Constants.SCREEN_WIDTH / 8))
            elif(x < 18):
                self.duration = random.randint(20, int(Constants.SCREEN_WIDTH / 6))
            else:
                self.duration = random.randint(50, int(Constants.SCREEN_WIDTH / 4))

            self.angle_inc = random.randint(5,self.duration)

            self.sign_x = self.get_rand_sign()
            self.sign_y = self.get_rand_sign()
            self.sign_z = self.get_rand_sign()

            new_random = random.random()
            self.vx = new_random * self.sign_x * 5
            angle_likely = random.randint(0,20)
            if angle_likely < 17:
                self.vy = (new_random / 2) * self.sign_y * 1
            else:
                self.vy = random.random() * self.sign_y * 2

            self.vz = (random.random() * self.sign_z) / 10

            print("vz" + str(self.vz))

        self.duration = self.duration - 1

        z_speed = ((60 + self.z) / 120.0) / 3

        self.x = self.x + (self.vx * z_speed)
        self.y = self.y + (self.vy * z_speed)
        self.z = self.z + (self.vz * z_speed)

        cur_x = self.x
        cur_y = self.y
        cur_z = self.z

        if cur_y < self.min_y:
            self.y = self.min_y
        elif cur_y > maxY(cur_z):
            self.y = maxY(cur_z)

        if cur_x < -90:
            self.x = -90
        elif cur_x > self.max_x:
            self.x = self.max_x

        if cur_z < 0:
            self.z = 0
        elif cur_z > 63:
            self.z = 63

    def get_rand_sign(self) -> int:
        if random.randint(0, 1) == 0:
            return -1
        else:
            return 1

    def get_rand_sign_x(self) -> int:
        if random.randint(0, 1) == 0:
            return -1
        else:
            return 1

    def get_rand_sign_y(self) -> int:
        if random.randint(0, 20) < self.negative_y + 1:
            return 1
        else:
            return -1
