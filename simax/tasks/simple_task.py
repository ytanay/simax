from simax.features.vector import Vector
from simax.tasks.base_task import BaseTask


class SimpleTask(BaseTask):
    def __init__(self, giver, cycles=10):
        super().__init__()
        self.cycles = cycles
        self.giver = giver

    def cycle(self):
        if self.cycles:
            self.cycles -= 1
            return Vector(energy=-.000001, **{
                ("interest-%s" % self.giver.id): -.00001
            })

    def describe(self):
        return 'cycles=%d' % self.cycles