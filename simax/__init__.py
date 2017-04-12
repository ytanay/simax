import random
import time

from entitiy.park import Park
from person.person import Person
from world.world import World

world = World()
import os

clear = lambda: os.system('cls')

for _ in range(5):
    world.assign(Person(*world.random_placement()))

for _ in range(3):
    world.assign(Park(*world.random_placement()))


while True:

    world.draw_and_cycle()

    #input()
    time.sleep(0.2)
    clear()