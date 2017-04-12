from features.physical_object import PhysicalObject


class InfrastructureObject(object): pass


class Road(InfrastructureObject):

    SHAPE = 'line'
    COLOR = 'grey'

    def __init__(self, x0, y0, x1, y1):
        self.x0 = round(x0)
        self.y0 = round(y0)
        self.x1 = round(x1)
        self.y1 = round(y1)

        self.vertical = self.x0 == self.x1
        self.slope, self.intercept = self.params()

        self.intersections = set()

    def intersection(self, existing_road: 'Road') -> 'Intersection':
        if self.vertical or existing_road.vertical:
            return self.vertical_intersection(existing_road)

        if existing_road.slope == self.slope:
            return None

        x = (self.intercept - existing_road.intercept) / (existing_road.slope - self.slope)
        y = self.compute_y(x)
        if self.contains(x) and existing_road.contains(x):
            return Intersection(round(x), round(y))

    def params(self):
        if self.vertical:
            return None, None
        slope = (self.y1 - self.y0) / (self.x1 - self.x0)
        intercept = self.y0 - self.x0 * slope
        return slope, intercept

    def compute_x(self, y):
        return (y - self.intercept) / self.intercept

    def compute_y(self, x):
        return x * self.slope + self.intercept

    def contains(self, x):
        return min(self.x0, self.x1) - 0.02 <= x <= max(self.x0, self.x1) + 0.02

    def vertical_intersection(self, existing_road):
        if self.vertical and existing_road.vertical:
            if self.x0 == existing_road.x0:
                raise ValueError('Lines {} and {} converge'.format(self, existing_road))
            return

        vertical = self if self.vertical else existing_road
        other = self if vertical is not self else existing_road
        if other.contains(vertical.x0):
            return Intersection(round(vertical.x0), round(other.compute_y(vertical.x0)))


class Intersection(PhysicalObject, InfrastructureObject):
    COLOR = 'pink'

    def describe(self):
        return '{},{}'.format(self.x, self.y)

    def __lt__(self, other):
        return False


class VerticalRoad(Road):

    def __init__(self, x, y0, y1):
        super(VerticalRoad, self).__init__(x, y0, x, y1)


class HorizontalRoad(Road):

    def __init__(self, y, x0, x1):
        super(HorizontalRoad, self).__init__(x0, y, x1, y)