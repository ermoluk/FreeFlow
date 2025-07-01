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
        for other in nodes:
            if node != other and node.distance_to(other) <= radius:
                node.add_neighbor(other)