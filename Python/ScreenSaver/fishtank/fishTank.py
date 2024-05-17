import pygame as pg
from pygame.locals import *
import os
import random
import Constants
from Animals.Fish.Fish import Fish
from Images.FishImageHolder import FishImageHolder
from Images.SubImageHolder import SubImageHolder
from Images.Shadow import Shadow
from Behaviors.SmootheBehavior import SmootheBehavior
from Behaviors.Mechanical import Mechanical
from Animals.Fish.CatFish import CatFish
from Behaviors.RagDoll import RagDoll

def addFish(lst_fish, max_x: int = Constants.SCREEN_WIDTH, max_y: int = Constants.SCREEN_HEIGHT):

    for cur_fish in lst_fish:
        n = random.randint(0, 63)
        x = random.randint(0, max_x)
        y = random.randint(0, max_y)
        z = 50 - (n % 63)
        new_shadow = Shadow(x, y, z)
        lst_size = len(lst_fish)

        if (lst_fish[n % lst_size])[1] == 1:
            new_fish = CatFish(n, (x, y, z), new_shadow, cur_fish[0], group, SmootheBehavior(n))
            new_fish.setBehavior()
        elif (lst_fish[n % lst_size])[1] == 2:
            new_fish = Fish(n, (x, y, z), new_shadow, cur_fish[0], group, Mechanical(n))
        elif (lst_fish[n % lst_size])[1] == 3:
            new_fish = Fish(n, (x, y, z), new_shadow, cur_fish[0], group, RagDoll(n))
        else:
            new_fish = Fish(n, (x, y, z), new_shadow, cur_fish[0], group, SmootheBehavior(n))
        x = random.randint(new_fish.behavior.min_x, new_fish.behavior.max_x)
        y = random.randint(int(new_fish.behavior.min_y) + 10, int(new_fish.behavior.max_y) )
        z = 50 - (n % 63)
        new_fish.setPos(x, y, z)

        group.add(new_fish)
        listFish.append(new_fish)
        listShadow.append(new_shadow)
        group.add(new_fish)
        group.add(new_shadow)


# Initialise pygame
pg.init()

screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)

#screen = pg.display.set_mode([Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT])

Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT =screen.get_size()

# Create sprites
listFish = []
listShadow = []

#all_sprites = pg.sprite.LayeredUpdates()

group = pg.sprite.LayeredUpdates()

lstFishPiranha = []
lstFishGoofy = []
lstFishCatfish = []
lstSubs = []
lstDead = []

lstDead.append((FishImageHolder("ball.png"), 3))
lstSubs.append((SubImageHolder("yellow_submarine.png"), 2))

lstFishPiranha.append((FishImageHolder(), None))
lstFishGoofy.append((FishImageHolder("goldfish.png"), None))
lstFishGoofy.append((FishImageHolder("homer.png"), None))
lstFishGoofy.append((FishImageHolder("wanda.png"), None))
#lstFishGoofy.append((FishImageHolder("yellow_submarine.png"), 2))
lstFishGoofy.append((FishImageHolder("Mermaid.png"), None))
#lstFishGoofy.append((FishImageHolder("yellow_submarine.png"), 2))
lstFishCatfish.append((FishImageHolder("catfish.png"), 1))

for n in range(0, 100):
    addFish(lstFishPiranha, Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT)

for n in range(0,5):
    addFish(lstFishGoofy, Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT)

for n in range(0, 20):
    addFish(lstFishCatfish, Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT * .25)

for n in range(0, 20):
    addFish(lstSubs, Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT * .25)

for n in range(0, 20):
    addFish(lstDead, Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT * .25)

# Main loop, run until window closed
running = True
bg = pg.image.load(os.path.join('resources', "the_fish_tank.png"))
bg = pg.transform.scale(bg, (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
screen.blit(bg, (0, 0))
n = 0

clock=pg.time.Clock()

Constants.SCREEN_HEIGHT3RD = Constants.SCREEN_HEIGHT * .70

feeding = False

while running:

    clock.tick(64)

    # Check events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            running = False
        elif event.type == KEYDOWN:
            #print("This:" + str(event.key))
            if event.key != 1073741907 and event.key != K_f:
                running = False
            else:
                feeding = True

    for fish in listFish:
        fish.move()

    screen.blit(bg, (0, 0))

    group.draw(screen)

    pg.display.flip()





# close pygame
pg.quit()


