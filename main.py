import matplotlib.pyplot as plt
import random
import time

# ===============================
# Router Class
# ===============================
class Router:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = []

    def add_neighbor(self, router):
        self.neighbors.append(router)

    def __repr__(self):
        return f"Router({self.x}, {self.y})"


# ===============================
# Create 2D Mesh Network
# ===============================
def create_mesh(rows, cols):
    mesh = [[Router(i, j) for j in range(cols)] for i in range(rows)]

    for i in range(rows):
        for j in range(cols):
            r = mesh[i][j]

            # Connect north
            if i > 0:
                r.add_neighbor(mesh[i - 1][j])

            # Connect south
            if i < rows - 1:
                r.add_neighbor(mesh[i + 1][j])

            # Connect west
            if j > 0:
                r.add_neighbor(mesh[i][j - 1])

            # Connect east
            if j < cols - 1:
                r.add_neighbor(mesh[i][j + 1])

    return mesh

# ===============================
# Print Mesh Routers & Neighbors
# ===============================
def print_mesh(mesh):
    print("\n--- Mesh Connectivity ---")
    for row in mesh:
        for r in row:
            print(f"{r} -> {[str(n) for n in r.neighbors]}")
    print("-------------------------\n")

# ===============================
# Deterministic XY Routing
# ===============================
def xy_routing(mesh, src, dst):
    path = [src]
    current_x, current_y = src.x, src.y
    dest_x, dest_y = dst.x, dst.y

    # Move in X direction
    while current_x != dest_x:
        if dest_x > current_x:
            current_x += 1
        else:
            current_x -= 1
        path.append(mesh[current_x][current_y])

    # Move in Y direction
    while current_y != dest_y:
        if dest_y > current_y:
            current_y += 1
        else:
            current_y -= 1
        path.append(mesh[current_x][current_y])

    return path

# ===============================
# Visualization Functions
# ===============================
def draw_mesh(ax, mesh):
    rows, cols = len(mesh), len(mesh[0])

    # Draw routers
    for i in range(rows):
        for j in range(cols):
            r = mesh[i][j]
            ax.scatter(j, rows - 1 - i, color="skyblue", s=400, edgecolors="black")
            ax.text(j, rows - 1 - i, f"({i},{j})", ha="center", va="center", fontsize=10)

    # Draw links
    for i in range(rows):
        for j in range(cols):
            r = mesh[i][j]
            for n in r.neighbors:
                ax.plot([r.y, n.y],
                        [rows - 1 - r.x, rows - 1 - n.x],
                        color="gray", linewidth=1)


def animate_packet(ax, path, rows):
    for r in path:
        x, y = r.y, rows - 1 - r.x
        ax.scatter(x, y, color="red", s=400, edgecolors="black")
        plt.pause(0.5)
        ax.scatter(x, y, color="skyblue", s=400, edgecolors="black")

# ===============================
# Main Program
# ===============================
if __name__ == "__main__":
    ROWS, COLS = 4, 4
    mesh = create_mesh(ROWS, COLS)

    print("\n Mesh created successfully!\n")
    print_mesh(mesh)

    # Random src and dst
    src_x = random.randint(0, ROWS - 1)
    src_y = random.randint(0, COLS - 1)
    dst_x = random.randint(0, ROWS - 1)
    dst_y = random.randint(0, COLS - 1)

    while (src_x, src_y) == (dst_x, dst_y):
        dst_x = random.randint(0, ROWS - 1)
        dst_y = random.randint(0, COLS - 1)

    src = mesh[src_x][src_y]
    dst = mesh[dst_x][dst_y]

    print(f"Routing packet from {src} to {dst}\n")

    # XY Routing
    path = xy_routing(mesh, src, dst)
    print("Path:", " -> ".join(str(r) for r in path))

    # Visualization
    fig, ax = plt.subplots(figsize=(6, 6))
    draw_mesh(ax, mesh)
    animate_packet(ax, path, ROWS)
    plt.show()
