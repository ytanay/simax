from simax.entity.base_entity import BaseEntity
from simax.features.vector import Vector
from simax.tasks.simple_task import SimpleTask


class Park(BaseEntity):

    CHAR_REPR = 'P'
    COLOR = 'green'

    def __init__(self, x, y):
        super().__init__(x, y)

    def cycle(self):
        pass

    def get_vector(self):
        return Vector(nature=0.8)

    def request_task(self):
        return SimpleTask(self)