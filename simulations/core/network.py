import random
from core.node import Node

def generate_nodes(count, area_size=100):
    nodes = []
    for i in range(count):
        pos = (random.uniform(0, area_size), random.uniform(0, area_size))
        nodes.append(Node(i, pos))
    return nodes

def connect_neighbors(nodes, radius=40):
    for node in nodes:
        for other in nodes:
            if node != other and node.distance_to(other) <= radius:
                node.add_neighbor(other)

def find_shortest_path(start_node, end_node):
    from collections import deque

    visited = set()
    queue = deque()
    queue.append((start_node, [start_node]))

    while queue:
        current_node, path = queue.popleft()
        if current_node == end_node:
            return path

        visited.add(current_node)

        for neighbor in current_node.neighbors:
            if neighbor not in visited and neighbor not in path:
                queue.append((neighbor, path + [neighbor]))

    return None