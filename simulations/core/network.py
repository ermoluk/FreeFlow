import random
from core.node import Node

def generate_nodes(count, area_size=100):
    nodes = []
    for i in range(count):
        pos = (random.uniform(0, area_size), random.uniform(0, area_size))
        nodes.append(Node(i, pos))
    return nodes

def connect_neighbors(nodes, radius=30):
    for node in nodes:
        node.neighbors = []
        for other in nodes:
            if node != other and node.distance_to(other) <= radius:
                node.add_neighbor(other)

def find_path(start_node, end_node):
    from collections import deque

    if not start_node.online or not end_node.online:
        return None

    visited = set()
    queue = deque()
    queue.append((start_node, [start_node]))

    while queue:
        current_node, path = queue.popleft()
        if current_node == end_node:
            return path

        visited.add(current_node)

        for neighbor in current_node.neighbors:
            if neighbor not in visited and neighbor.online:
                queue.append((neighbor, path + [neighbor]))

    return None

def random_toggle(nodes, probability=0.2):
    for node in nodes:
        if random.random() < probability:
            node.toggle_status()