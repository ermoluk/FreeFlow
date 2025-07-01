from core.network import generate_nodes, connect_neighbors

nodes = generate_nodes(10)
connect_neighbors(nodes)

for node in nodes:
    print(f"Node {node.id} has neighbors: {[n.id for n in node.neighbors]}")