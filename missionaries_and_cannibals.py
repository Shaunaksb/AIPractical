from collections import deque

# State: (M_left, C_left, Boat_position)
# Boat_position: 1 = left side, 0 = right side

def is_valid(state):
    M_left, C_left, _ = state
    M_right = 3 - M_left
    C_right = 3 - C_left

    # Missionaries should not be outnumbered
    if (M_left > 0 and C_left > M_left):
        return False
    if (M_right > 0 and C_right > M_right):
        return False

    return True

def get_next_states(state):
    M, C, boat = state
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]  # possible boat moves
    next_states = []

    for m, c in moves:
        if boat == 1:  # moving from left to right
            new_state = (M - m, C - c, 0)
        else:  # moving from right to left
            new_state = (M + m, C + c, 1)

        if 0 <= new_state[0] <= 3 and 0 <= new_state[1] <= 3:
            if is_valid(new_state):
                next_states.append(new_state)

    return next_states

def bfs():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    queue = deque([(start, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path + [current]

        for next_state in get_next_states(current):
            queue.append((next_state, path + [current]))

    return None

# Run solution
solution = bfs()

# Print steps
if solution:
    for step in solution:
        print(step)
else:
    print("No solution found")