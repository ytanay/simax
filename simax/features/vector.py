class Vector(object):
    SHORTHAND = 'V'

    def __init__(self, **kwargs):
        super(Vector, self).__init__()
        self.vector = kwargs

    def dot(self, other):
        product = 0
        for member, value in self.vector.items():
            product += value * other.member(member)
        return product

    def apply(self, other):
        for member, effect in other.vector.items():
            value = self.member(member)
            self.vector[member] = value + effect

    def member(self, name, default=0):
        return self.vector.get(name, default)

    def __str__(self):
        return '%s(%s)' % (self.SHORTHAND, ','.join(['%s=%.3f' % (key, value) for key, value in self.vector.items()]))