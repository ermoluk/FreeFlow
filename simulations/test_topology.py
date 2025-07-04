import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle
from matplotlib.lines import Line2D
from core.network import (
    generate_nodes,
    connect_neighbors,
    find_shortest_path_weighted,
    find_clusters,
    simulate_random_transactions,
    sync_journals,
    simulate_failures,
    global_log,
    save_global_log
)
import numpy as np

# Generate 100 nodes in a 200x200 area
nodes = generate_nodes(100, area_size=200)
radius = 30
active_transactions = []

def update(frame):
    plt.clf()

    # Move nodes and toggle online/offline status randomly
    for node in nodes:
        if not node.failed:
            node.move()
            node.toggle_status(probability=0.05)

    # Simulate network failures (clusters and Bridge Nodes)
    simulate_failures(nodes, frame)

    # Connect neighbors and find clusters
    connect_neighbors(nodes, radius)
    clusters = find_clusters(nodes)

    # Synchronize journals within clusters
    sync_journals(clusters)

    # Simulate random transactions
    simulate_random_transactions(nodes, active_transactions, probability=0.1)

    # Update transaction lifetimes
    for tx in active_transactions:
        tx["frames_left"] -= 1
    active_transactions[:] = [tx for tx in active_transactions if tx["frames_left"] > 0]

    # Find shortest path from first to last node
    start, end = nodes[0], nodes[-1]
    path, total_cost = find_shortest_path_weighted(start, end)

    # Metrics: % offline nodes, avg PoC credits
    offline_count = sum(1 for n in nodes if not n.online or n.failed)
    avg_poc = np.mean([n.credits for n in nodes if n.online and not n.failed]) if nodes else 0
    total_nodes = len(nodes)
    offline_percent = (offline_count / total_nodes) * 100

    plt.title(f"Frame {frame} | Offline: {offline_percent:.1f}% | Avg PoC: {avg_poc:.1f}")

    # Draw clusters as transparent circles
    colors = plt.cm.tab20(np.linspace(0, 1, len(clusters)))
    for i, cluster in enumerate(clusters):
        cluster_center = np.mean([n.position for n in cluster], axis=0)
        cluster_circle = Circle(cluster_center, radius=25, color=colors[i], alpha=0.1, zorder=0)
        plt.gca().add_patch(cluster_circle)

    # Draw connections
    for node in nodes:
        for neighbor in node.neighbors:
            if neighbor.online and node.online and not neighbor.failed and not node.failed:
                plt.plot([node.position[0], neighbor.position[0]],
                         [node.position[1], neighbor.position[1]],
                         color="lightgray", linewidth=0.4, alpha=0.5, zorder=1)

    # Draw nodes
    for node in nodes:
        size = 30 + node.credits * 2
        if node.failed:
            color = "black"
        else:
            color = "gold" if node.is_bridge else ("green" if node.online else "red")
        plt.scatter(*node.position, color=color, s=size, alpha=0.8, edgecolors='black', zorder=3)
        plt.text(node.position[0], node.position[1], f"{node.id}", fontsize=5, ha='center', zorder=4)

    # Draw path if exists
    if path:
        for i in range(len(path)-1):
            p1, p2 = path[i].position, path[i+1].position
            plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color="blue", linewidth=2, zorder=5)

    # Draw global mini-map
    ax_inset = plt.gcf().add_axes([0.7, 0.7, 0.25, 0.25])
    ax_inset.set_xlim(0, 200)
    ax_inset.set_ylim(0, 200)
    ax_inset.axis('off')
    for node in nodes:
        mini_color = "black" if node.failed else ("green" if node.online else "red")
        ax_inset.scatter(*node.position, color=mini_color, s=5)

    # Add legend
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', label='Regular Node',
               markerfacecolor='green', markersize=6),
        Line2D([0], [0], marker='o', color='w', label='Bridge Node',
               markerfacecolor='gold', markersize=6),
        Line2D([0], [0], marker='o', color='w', label='Offline/Failed Node',
               markerfacecolor='black', markersize=6),
        Line2D([0], [0], color='lightgray', lw=1, label='Connection'),
        Line2D([0], [0], color='blue', lw=2, label='Path')
    ]
    plt.legend(handles=legend_elements, loc='lower left', fontsize=6)

# Create animation
fig = plt.figure(figsize=(10,10))
ani = animation.FuncAnimation(fig, update, frames=500, interval=300)
plt.show()

# Save global log
save_global_log("log.txt")
print("\nGlobal log saved to log.txt ✅")