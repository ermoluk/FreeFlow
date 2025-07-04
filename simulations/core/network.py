import random
from core.node import Node
import heapq
import datetime

# Global event log
global_log = []

# Probability of packet loss (simulated network degradation)
PACKET_LOSS_PROB = 0.1

def generate_nodes(count, area_size=100):
    nodes = []
    for i in range(count):
        pos = (random.uniform(0, area_size), random.uniform(0, area_size))
        nodes.append(Node(i, pos, area_size))
    return nodes

def connect_neighbors(nodes, radius=30):
    for node in nodes:
        node.neighbors.clear()
        for other in nodes:
            if node != other and node.distance_to(other) <= radius:
                node.add_neighbor(other)

def find_clusters(nodes):
    visited = set()
    clusters = []

    def dfs(node, cluster):
        visited.add(node)
        cluster.append(node)
        for neighbor in node.neighbors:
            if neighbor not in visited and neighbor.online and not neighbor.failed:
                dfs(neighbor, cluster)

    for node in nodes:
        if node.online and not node.failed and node not in visited:
            cluster = []
            dfs(node, cluster)
            clusters.append(cluster)

    # Assign cluster IDs and mark Bridge Nodes
    for cluster_id, cluster in enumerate(clusters, start=1):
        for node in cluster:
            border = any(n.cluster_id and n.cluster_id != cluster_id for n in node.neighbors)
            node.update_cluster(cluster_id, bridge=border)

    return clusters

def find_shortest_path_weighted(start_node, end_node):
    if not start_node.online or not end_node.online or start_node.failed or end_node.failed:
        return None, None

    queue = [(0, start_node, [start_node])]
    visited = set()

    while queue:
        cost, current_node, path = heapq.heappop(queue)
        if current_node == end_node:
            return path, cost
        visited.add(current_node)
        for neighbor in current_node.neighbors:
            if neighbor not in visited and neighbor.online and not neighbor.failed:
                total_cost = cost + current_node.distance_to(neighbor)
                heapq.heappush(queue, (total_cost, neighbor, path + [neighbor]))
    return None, None

def simulate_random_transactions(nodes, active_transactions, probability=0.2):
    online_nodes = [n for n in nodes if n.online and not n.failed]
    if len(online_nodes) < 2:
        return
    for node in online_nodes:
        if random.random() < probability:
            recipient = random.choice(online_nodes)
            if recipient != node:
                if random.random() > PACKET_LOSS_PROB:
                    # Successful transaction
                    node.log_transaction(recipient)
                    active_transactions.append({
                        "from": node,
                        "to": recipient,
                        "frames_left": 10
                    })
                    global_log.append(f"TX: {node.address} → {recipient.address}")
                else:
                    # Simulated packet loss
                    global_log.append(f"PACKET DROPPED: {node.address} → {recipient.address}")

def sync_journals(clusters):
    for cluster in clusters:
        combined_journal = []
        for node in cluster:
            combined_journal.extend(node.journal)
        for node in cluster:
            node.journal = list(set(combined_journal))  # Remove duplicates

def simulate_failures(nodes, frame, cluster_failure_interval=100, bridge_failure_interval=50):
    # Fail a random cluster every cluster_failure_interval frames
    if frame % cluster_failure_interval == 0:
        clusters = find_clusters(nodes)
        if clusters:
            failed_cluster = random.choice(clusters)
            for node in failed_cluster:
                node.failed = True
            global_log.append(f"CLUSTER FAILURE: Cluster {failed_cluster[0].cluster_id} failed")

    # Fail a random Bridge Node every bridge_failure_interval frames
    if frame % bridge_failure_interval == 0:
        bridge_nodes = [n for n in nodes if n.is_bridge and n.online and not n.failed]
        if bridge_nodes:
            failed_node = random.choice(bridge_nodes)
            failed_node.failed = True
            global_log.append(f"BRIDGE FAILURE: Node {failed_node.id} failed")

def log_event(event):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    global_log.append(f"[{timestamp}] {event}")

def save_global_log(filename="log.txt"):
    with open(filename, "w") as f:
        f.write("=== FreeFlow Simulation Detailed Log ===\n\n")
        for entry in global_log:
            f.write(entry + "\n")
    print(f"✅ Super-detailed log saved to {filename}")