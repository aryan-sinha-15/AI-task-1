#Implement AI based intelligence agent to solve the water jet problem

from collections import deque

# Jug capacities
JUG1_CAPACITY, JUG2_CAPACITY, TARGET = 3, 5, 4

def bfs():
    visited = set()
    queue = deque([(0, 0)])  # Start with both jugs empty

    while queue:
        jug1, jug2 = queue.popleft()
        print(f"{jug1} {jug2}")  # Output current state

        if jug1 == TARGET or jug2 == TARGET:  # Goal check
            print("Goal reached!")
            return
        
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))

        # Possible actions
        queue.extend([
            (JUG1_CAPACITY, jug2),  # Fill Jug1
            (jug1, JUG2_CAPACITY),  # Fill Jug2
            (0, jug2),              # Empty Jug1
            (jug1, 0),              # Empty Jug2
            (max(jug1 - (JUG2_CAPACITY - jug2), 0), min(jug2 + jug1, JUG2_CAPACITY)),  # Pour Jug1 -> Jug2
            (min(jug1 + jug2, JUG1_CAPACITY), max(jug2 - (JUG1_CAPACITY - jug1), 0))   # Pour Jug2 -> Jug1
        ])

bfs()
