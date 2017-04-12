import random
from collections import defaultdict

from simax.features.moveable_object import MovableObject
from simax.navigation.pathfinding import Pathfinder
from simax.navigation.topology import Topology
from simax.utils.math_utils import linear_interpolation
from simax.utils.singleton import Singleton


def safe_choose(x, y, key):
    if x is None:
        return y
    if y is None:
        return x
    return key(x, y)


def random_color():
    return "#%02x%02x%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


class World(object, metaclass=Singleton):

    WIDTH = 500
    HEIGHT = 500

    def __init__(self, canvas):
        self.entities = []
        self.canvas = canvas
        self.entity_map = {}
        self.lines = defaultdict(list)
        self.cycles = 0
        self.topology = Topology()
        self.pathfinder = Pathfinder(self.topology)

    def draw_and_cycle(self):
        self.cycles += 1
        statuses = []
        for id, entity in self.entity_map.items():
            statuses.append(entity.cycle())

            self.canvas.coords(id, entity.x-5, entity.y-5, entity.x + 5, entity.y + 5)

            min_attraction, max_attraction = None, None
            for friend, line in self.lines[id]:
                min_attraction = safe_choose(min_attraction, entity.attraction(friend), min)
                max_attraction = safe_choose(max_attraction, entity.attraction(friend), max)

            if min_attraction is None:
                min_attraction = -1

            if max_attraction is None:
                min_attraction = 1


            for friend, line in self.lines[id]:
                _, _, friend_x, friend_y = self.canvas.coords(line)
                self.canvas.coords(line, entity.x, entity.y, friend_x, friend_y)
                if max_attraction == min_attraction:
                    color = (150 + 20) // 2
                else:
                    color = round(
                        linear_interpolation(entity.attraction(friend), min_attraction, 150, max_attraction, 20))
               # width = linear_interpolation(entity.attraction(friend), min_attraction, 0.5, max_attraction, 3)

                self.canvas.itemconfig(line, fill="#%02x%02x%02x" % (color, color, color))

        return statuses

    def assign(self, entity):
        if not (0 <= entity.x <= self.WIDTH and 0 <= entity.y <= self.HEIGHT):
            raise ValueError('Entity %s out of range' % entity)
        self.entities.append(entity)
        oval = self.canvas.create_oval(entity.x-5, entity.y-5, entity.x + 5, entity.y + 5, fill=entity.COLOR, tags='person')
        #self.canvas.create_text(entity.x, entity.y + 10,
        #                        text='{}:{}({},{})'.format(entity.CHAR_REPR, entity.id, entity.x, entity.y))
        self.entity_map[oval] = entity

    def prepare(self):
        for id, entity in self.entity_map.items():
            if isinstance(entity, MovableObject):
                for friend in [entity for entity in self.entities if not isinstance(entity, MovableObject)]:
                    self.lines[id].append((friend, self.canvas.create_line(entity.x, entity.y, friend.x, friend.y, width=1.5)))

        for road in self.topology.roads:
            line = self.canvas.create_line(road.x0, road.y0, road.x1, road.y1, width=10, fill="grey")

        for base, targets in self.topology.graph.items():
            for target in targets:
                self.canvas.create_line(base.x, base.y, target.x, target.y, width=3, fill=random_color())

        for intersection in self.topology.intersections:
            self.canvas.create_oval(intersection.x - 5, intersection.y - 5, intersection.x + 5, intersection.y + 5, fill=intersection.COLOR)
            self.canvas.create_text(intersection.x, intersection.y + 10, text='I:{}({},{})'.format(intersection.id, intersection.x, intersection.y))

        self.canvas.tag_raise('person')

    def cycle(self):
        pass

    def stringify(self, entities):
        if len(entities) > 1:
            return '#'
        if len(entities) == 1:
            return entities[0].CHAR_REPR
        return '.'

    def random_placement(self):
        return random.randint(0, self.WIDTH), random.randint(0, self.HEIGHT)

