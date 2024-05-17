from Animals.Fish.Fish import Fish
import Constants

class CatFish(Fish):

    def setBehavior(self):
        self.behavior.setMinY(Constants.SCREEN_HEIGHT - (.45 * Constants.SCREEN_HEIGHT))
        self.behavior.negative_y = 18