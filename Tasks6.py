#8puzzzle

import heapq

goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Goal state

# Heuristic function (Manhattan Distance)
def heuristic(state):
    return sum(abs(i - (val - 1) // 3) + abs(j - (val - 1) % 3) for i, row in enumerate(state) for j, val in enumerate(row) if val)

# Find empty tile position
def find_empty(state):
    for i, row in enumerate(state):
        for j, val in enumerate(row):
            if val == 0: return i, j

# Generate new states by moving the empty tile
def move(state, x, y, dx, dy):
    nx, ny = x + dx, y + dy
    if 0 <= nx < 3 and 0 <= ny < 3:
        new_state = [row[:] for row in state]
        new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
        return new_state

# A* Algorithm
def solve_8_puzzle(initial):
    pq, visited = [(heuristic(initial), initial, [])], set()
    while pq:
        _, state, path = heapq.heappop(pq)
        if state == goal: return path + [state]
        visited.add(tuple(map(tuple, state)))
        x, y = find_empty(state)
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            new_state = move(state, x, y, dx, dy)
            if new_state and tuple(map(tuple, new_state)) not in visited:
                heapq.heappush(pq, (len(path) + heuristic(new_state), new_state, path + [state]))

# Initial state (random disorder)
initial = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]

# Solve and print solution steps
for step in solve_8_puzzle(initial):
    for row in step: print(row)
    print("↓")
