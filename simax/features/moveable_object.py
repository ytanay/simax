import math

from entitiy.base_entity import BaseEntity
from features.physical_object import PhysicalObject
from utils import math_utils


class MovableObject(BaseEntity):

    def __init__(self, x, y, **kwargs):
        super(MovableObject, self).__init__(x, y, **kwargs)
        self.target = None
        self.target_segment = None
        self.current_location = None

        self.path = None

    def move_towards(self):

        if not self.target:
            return None

        if self.nearby(self.target): # End goal
            self.current_location = self.target
            self.x, self.y = self.target.x, self.target.y
            self.target = None
            return 'arrived at target %s' % self.current_location

        if self.nearby(self.target_segment) or not self.target_segment:
            self.target_segment = self.path.pop(0) if self.path else self.target
            return 'switching target segment to {}'.format(self.target_segment)

        line = (self.target_segment.x - self.x, self.target_segment.y - self.y)
        dist = self.distance(self.target_segment)
        self.x += 1 * line[0] / dist
        self.y += 1 * line[1] / dist

        return 'moving towards target %s' % self.target
