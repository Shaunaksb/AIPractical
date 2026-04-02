from collections import deque

def bfs_water_jug(c1, c2, target):
    queue = deque([(0, 0)]) # Start with empty jugs
    visited = set([(0, 0)]) # Track seen states
    steps=0

    while queue:
        j1, j2 = queue.popleft()

        print(j1,j2)
        steps+=1
        if j1 == target or j2 == target:
            return f"Target Reached!, steps: {steps}" 

        # Define the moves
        moves = [
            (c1, j2), (j1, c2), # Fill
            (0, j2), (j1, 0),   # Empty
            (j1 - min(j1, c2 - j2), j2 + min(j1, c2 - j2)), # Pour J1 -> J2
            (j1 + min(j2, c1 - j1), j2 - min(j2, c1 - j1))  # Pour J2 -> J1
        ]

        for move in moves:
            if move not in visited:
                visited.add(move)
                queue.append(move)
                
    return f"No solution, steps: {steps}"

print(bfs_water_jug(4, 3, 2))