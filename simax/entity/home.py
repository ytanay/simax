from simax.entity.base_entity import BaseEntity
from simax.features.vector import Vector
from simax.tasks.simple_task import SimpleTask


class Home(BaseEntity):

    CHAR_REPR = 'H'
    COLOR = 'blue'

    def __init__(self, x, y):
        super().__init__(x, y)

    def cycle(self):
        pass

    def get_vector(self):
        return Vector(energy=-1)

    def request_task(self):
        return SimpleTask(self)