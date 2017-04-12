from simax.entity.home import Home
from simax.entity.park import Park
from simax.person.person import Person
from simax.transport.road import HorizontalRoad
from simax.transport.road import VerticalRoad, Road


def seed_entities():
    yield Person(120, 100)
    yield Home(120, 120)
    yield Park(420, 300)
    yield Park(120, 380)


def seed_topology():
    yield VerticalRoad(100, 50, 450), \
          VerticalRoad(350, 50, 450), \
          VerticalRoad(600, 50, 450), \
          HorizontalRoad(250, 100, 600), \
          Road(350, 450, 600, 50), \
          Road(100, 450, 350, 50)
