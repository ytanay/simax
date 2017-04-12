from math import sqrt

from simax.features.trackable import Trackable


class PhysicalObject(Trackable):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def on(self, target):
        return target and self.x == target.x and self.y == target.y

    def nearby(self, target):
        return target and abs(self.x - target.x) <= 1 and abs(self.y - target.y) <= 1

    def distance(self, target):
        return sqrt((self.x - target.x) ** 2 + (self.y - target.y) ** 2)

    def normalized_distance(self, target):
        distance = self.distance(target)
        return 1 / distance if distance else 1