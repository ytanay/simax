from collections import defaultdict
from typing import List

from transport.road import Intersection, Road


class Topology(object):

    def __init__(self):
        self.intersections = set()
        self.roads = []
        self.graph = defaultdict(set)

    def add_road(self, road: Road) -> None:

        # Get tips
        road.intersections = {self.nearby_intersection(x) or x for x in (Intersection(road.x0, road.y0), Intersection(road.x1, road.y1))}
        for tip in road.intersections:
            self.add_intersection(tip, [road])

        for existing_road in self.roads:
            intersection = road.intersection(existing_road)
            if intersection is None:
                continue

            self.add_intersection(intersection, [road, existing_road])

        self.roads.append(road)

    def add_intersection(self, intersection: Intersection, roads: List[Road]) -> object:
        if intersection is None:
            return

        intersection = self.nearby_intersection(intersection) or intersection

        self.intersections.add(intersection)

        for road in roads:
            for neighbor_intersection in road.intersections:
                self.add_to_graph(intersection, neighbor_intersection)
            road.intersections.add(intersection)

        return intersection

    def add_to_graph(self, i1, i2):
        if i1 is i2:
            return
        self.graph[i1].add(i2)
        self.graph[i2].add(i1)

    def nearby_intersection(self, target):
        nearby = [intersection for intersection in self.intersections if intersection.distance(target) < 1 and intersection is not target]
        if len(nearby) > 1:
            raise ValueError('Multiple nearby intersections')

        if nearby:
            return nearby[0]

    def cost(self, node1, node2):
        return node1.distance(node2)