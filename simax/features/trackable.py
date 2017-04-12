from collections import defaultdict


class Trackable(object):
    COUNTER_BY_TYPE = defaultdict(lambda: 0)

    def __init__(self):
        self.id = self.COUNTER_BY_TYPE[type(self)]
        self.COUNTER_BY_TYPE[type(self)] += 1

    def __str__(self):
        return '%s:%s(%s)' % (type(self).__name__, self.id, self.describe())

    def __repr__(self):
        return self.__str__()

    def describe(self):
        return '?'