from features.physical_object import PhysicalObject


class BaseEntity(PhysicalObject):

    CHAR_REPR = '?'

    def __init__(self, x, y, **kwargs):
        super().__init__(x, y)
        self.vector = self.get_vector()

    def attraction(self, other):
        return self.state.member('interest-%s' % other.id, 1) * self.normalized_distance(other) * self.vector.dot(other.vector)

    def get_vector(self):
        raise NotImplementedError('Must implement get_vector')