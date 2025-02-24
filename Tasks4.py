from collections import deque

# Graph representation (Adjacency List)
graph = {
    'A': ['B', 'C', 'X'],
    'B': ['D', 'E'],
    'C': ['F', 'G', 'L'],
    'F': ['T'],
    'D': [],
    'E': [],
    'G': [],
    'L': [],
    'T': [],
    'X': []
}

# Depth-First Search (DFS)
def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    path.append(start)

    if start == goal:
        return path

    for neighbor in graph.get(start, []):
        if neighbor not in path:
            new_path = dfs(graph, neighbor, goal, path.copy())
            if new_path:
                return new_path
    return None

# Breadth-First Search (BFS)
def bfs(graph, start, goal):
    queue = deque([[start]])  # Initialize queue with the starting path

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        for neighbor in graph.get(node, []):
            if neighbor not in path:
                new_path = list(path) + [neighbor]
                queue.append(new_path)

    return None

# Initial and Goal State
initial_state = 'A'
goal_state = 'T'

# Run DFS and BFS
dfs_path = dfs(graph, initial_state, goal_state)
bfs_path = bfs(graph, initial_state, goal_state)

# Display results
print("DFS Path:", " -> ".join(dfs_path) if dfs_path else "No path found")
print("BFS Path:", " -> ".join(bfs_path) if bfs_path else "No path found")
