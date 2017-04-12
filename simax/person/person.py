from features.moveable_object import MovableObject
from features.vector import Vector
from person.preson_vectors import PersonalityVector, StateVector
from tasks.none_task import NoneTask
from world.world import World


class Person(MovableObject):

    CHAR_REPR = 'H'
    COLOR = 'red'

    def __init__(self, x, y):
        super().__init__(x, y)
        self.task = NoneTask()
        self.state = StateVector(energy=1)
        self.description = None

    def cycle(self):
        effect, description = self.compute_cycle()
        if effect:
            self.state.apply(effect)
        self.description = description
        return description

    def compute_cycle(self):
        move_status = self.move_towards()
        if move_status:
            return Vector(energy=-.000001), 'moving toward target %s' % move_status

        effect = self.task.cycle()
        if effect:
            return effect, 'performing task %s' % self.task
        elif self.current_location:
            if self.attraction(self.current_location) > 0:
                task = self.current_location.request_task()
                if task:
                    self.task = task
                    return None, 'acquired new task %s' % task

        self.target = self.pick_target()
        self.path = World().pathfinder.to(self, self.target)
        return None, 'selected target %s (%f)' % (self.target, self.attraction(self.target))

    def pick_target(self):
        return max([entity for entity in World().entities if not isinstance(entity, type(self))], key=lambda entity: self.attraction(entity))

    def get_vector(self):
        return PersonalityVector(nature=0.1, work=0.2)

    def describe(self):
        return '%s,%s: %s' % (self.vector, self.state, self.description)
