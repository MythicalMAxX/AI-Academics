# python program to solve water jug problem.

from collections import deque

# Define the state as a tuple (x, y) where x is the amount of water in jug1 and y is the amount of water in jug2
def is_valid_state(x, y, max1, max2):
    return 0 <= x <= max1 and 0 <= y <= max2

def bfs_solve(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque([(0, 0)])  # Initial state, both jugs are empty
    visited.add((0, 0))

    while queue:
        x, y = queue.popleft()
        
        if x == target or y == target or x + y == target:
            return True
        
        possible_states = [
            (jug1_capacity, y),  # Fill jug1
            (x, jug2_capacity),  # Fill jug2
            (0, y),              # Empty jug1
            (x, 0),              # Empty jug2
            (x - min(x, jug2_capacity - y), y + min(x, jug2_capacity - y)),  # Pour jug1 into jug2
            (x + min(y, jug1_capacity - x), y - min(y, jug1_capacity - x))   # Pour jug2 into jug1
        ]

        for state in possible_states:
            if state not in visited and is_valid_state(state[0], state[1], jug1_capacity, jug2_capacity):
                queue.append(state)
                visited.add(state)
    
    return False

# Example usage
jug1_capacity = 4
jug2_capacity = 3
target = 2

if bfs_solve(jug1_capacity, jug2_capacity, target):
    print(f"It is possible to get exactly {target} liters.")
else:
    print(f"It is not possible to get exactly {target} liters.")

