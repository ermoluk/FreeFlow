import random

class Node:
    def __init__(self, node_id, position):
        self.id = node_id
        self.position = position
        self.neighbors = []
        self.online = True
        self.journal = []  

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def distance_to(self, node):
        x1, y1 = self.position
        x2, y2 = node.position
        return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

    def toggle_status(self):
        self.online = not self.online
        status = "online" if self.online else "offline"
        self.journal.append(f"Node {self.id} toggled to {status}")

    def log_contact(self, other_node):
        self.journal.append(f"Contact with Node {other_node.id}")