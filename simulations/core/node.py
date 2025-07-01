class Node:
    def __init__(self, node_id, position):
        self.id = node_id
        self.position = position
        self.neighbors = []

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def distance_to(self, node):
        x1, y1 = self.position
        x2, y2 = node.position
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5