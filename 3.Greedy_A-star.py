
import time
import math

def find_neighbors(current, maze, visited):
    a, b = current
    neighbors = []

    rows = len(maze)
    cols = len(maze[0])

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    for dr, dc in directions:
        r = a + dr
        c = b + dc

        if 0 <= r < rows and 0 <= c < cols:
            if maze[r][c] != 1 and (r,c) not in visited:
                neighbors.append((r,c))

    return neighbors


def heuristic(node, goal):
    return math.sqrt((goal[0]-node[0])**2 +
                     (goal[1]-node[1])**2)


def search(algorithm):
    maze = [[0,0,0,0],
            [0,1,1,0],
            [0,0,0,0],
            [1,1,1,0]]

    start = (0,0)
    goal = (3,3)

    Q = [start]
    visited = set()
    parent = {start: None}
    cost = {start: 0}

    while len(Q) > 0:

        if algorithm == "greedy":
            Q.sort(key=lambda x: heuristic(x, goal))

        elif algorithm == "astar":
            Q.sort(key=lambda x: cost[x] + heuristic(x, goal))

        current = Q.pop(0)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            break

        neighbors = find_neighbors(current, maze, visited)

        for next_node in neighbors:

            new_cost = cost[current] + 1

            if next_node not in cost or new_cost < cost[next_node]:

                cost[next_node] = new_cost
                parent[next_node] = current
                Q.append(next_node)

    path = []

    if goal in parent:
        node = goal

        while node is not None:
            path.append(node)
            node = parent[node]

        path.reverse()

    return path, maze


def print_path_matrix(maze, path):
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if (r,c) in path:
                print("*", end=" ")
            else:
                print(maze[r][c], end=" ")
        print()


# Greedy Best First Search
st = time.perf_counter()
greedy_path, maze = search("greedy")
et = time.perf_counter()

print("GREEDY BEST FIRST SEARCH")
print_path_matrix(maze, greedy_path)
print("Path:", greedy_path)
print(f"Time = {et-st:.6f} seconds")

print()

# A* Search
st = time.perf_counter()
astar_path, maze = search("astar")
et = time.perf_counter()

print("A* SEARCH")
print_path_matrix(maze, astar_path)
print("Path:", astar_path)
print(f"Time = {et-st:.6f} seconds")
