from core.network import generate_nodes, connect_neighbors, find_path, random_toggle

nodes = generate_nodes(10, area_size=50)
connect_neighbors(nodes, radius=25)

for step in range(5):  
    print(f"\n=== Step {step+1} ===")
    random_toggle(nodes, probability=0.3)  
    connect_neighbors(nodes, radius=25)   

    start = nodes[0]
    end = nodes[-1]
    path = find_path(start, end)

    if path:
        print(f"Path from Node {start.id} to Node {end.id}: {[n.id for n in path]}")
        for node in path:
            node.log_contact(start)
            node.log_contact(end)
    else:
        print(f"No path between Node {start.id} and Node {end.id} (some nodes offline)")

print("\n=== Journals ===")
for node in nodes:
    print(f"Node {node.id} journal:")
    for entry in node.journal:
        print(f"  - {entry}")