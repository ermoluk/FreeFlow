from core.network import generate_nodes, connect_neighbors, find_shortest_path

nodes = generate_nodes(10)
connect_neighbors(nodes)

for node in nodes:
    print(f"Node {node.id} has neighbors: {[n.id for n in node.neighbors]}")

start = nodes[0]
end = nodes[9]
path = find_shortest_path(start, end)

if path:
    print(f"\nShortest path from Node {start.id} to Node {end.id}: {[n.id for n in path]}")
    print(f"Hops: {len(path) - 1}")
else:
    print(f"\nNo path found from Node {start.id} to Node {end.id}")