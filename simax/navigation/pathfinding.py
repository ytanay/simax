from queue import PriorityQueue, Queue


class Pathfinder(object):

    def __init__(self, topology):
        self.topology = topology

    def to(self, source, target):
        start, end = self.nearest_intersection(source), self.nearest_intersection(target)
        grid = self.dijkstra_search(start, end)
        path = self.reconstruct(grid, start, end)
        return path

    def nearest_intersection(self, entity):
        return min(self.topology.intersections, key=lambda x: x.distance(entity))

    def bfs(self, start, end):
        frontier = Queue()
        frontier.put(start)
        came_from = {start: None}

        while not frontier.empty():
            current = frontier.get()
            if current is end:
                break
            for neighbor in self.topology.graph[current]:
                if neighbor not in came_from:
                    frontier.put(neighbor)
                    came_from[neighbor] = current

        return came_from

    def dijkstra_search(self, start, end):
        frontier = PriorityQueue()
        frontier.put((0, start))
        came_from = {start: None}
        cost_so_far = {start: 0}

        while not frontier.empty():
            current = frontier.get()[1]

            if current == end:
                break

            for neighbor in self.topology.graph[current]:
                new_cost = cost_so_far[current] + self.topology.cost(current, neighbor)
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    frontier.put((new_cost, neighbor))
                    came_from[neighbor] = current

        return came_from

    def a_star(self, start, end):
        frontier = PriorityQueue()
        frontier.put(())

    @staticmethod
    def reconstruct(paths, start, end):
        path = [end]
        current = paths[end]
        while current is not start:
            path.append(current)
            current = paths[current]
        path.append(start)
        return list(reversed(path))
