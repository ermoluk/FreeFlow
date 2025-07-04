import random
import string

class Node:
    def __init__(self, node_id, position, area_size):
        self.id = node_id
        self.position = list(position)
        self.area_size = area_size
        self.neighbors = []
        self.online = True
        self.journal = []
        self.credits = 0  
        self.cluster_id = None  
        self.is_bridge = False  
        self.address = None
        self.failed = False  

    def generate_address(self):
        suffix = ''.join(random.choices(string.hexdigits.lower(), k=4))
        return f"ff://{self.cluster_id}/{self.id}/{suffix}"

    def update_cluster(self, cluster_id, bridge=False):
        if self.cluster_id != cluster_id:
            self.cluster_id = cluster_id
            self.is_bridge = bridge
            self.address = self.generate_address()
            status = "Bridge Node" if bridge else "Regular Node"
            self.journal.append(f"Assigned to cluster {cluster_id} as {status}")

    def add_neighbor(self, node):
        if node not in self.neighbors:
            self.neighbors.append(node)

    def distance_to(self, node):
        x1, y1 = self.position
        x2, y2 = node.position
        return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

    def toggle_status(self, probability=0.05):
        if random.random() < probability:
            self.online = not self.online
            status = "online" if self.online else "offline"
            self.journal.append(f"Node {self.address} toggled to {status}")

    def move(self, step_size=2):
        if self.online:
            dx, dy = random.uniform(-step_size, step_size), random.uniform(-step_size, step_size)
            self.position[0] = min(max(0, self.position[0] + dx), self.area_size)
            self.position[1] = min(max(0, self.position[1] + dy), self.area_size)

    def log_transaction(self, recipient):
        if self.online and recipient.online:
            tx_id = ''.join(random.choices(string.hexdigits.lower(), k=8))
            entry = f"TX:{tx_id} from {self.address} to {recipient.address}"
            self.journal.append(entry)
            recipient.journal.append(entry)
            self.credits += 2  
            recipient.credits += 1