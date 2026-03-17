import heapq

def get_manhattan_distance(state, goal):
    distance = 0
    for i in range(len(state)):
        if state[i] != 0:  # Skip the empty tile
            # Current coordinates
            curr_row, curr_col = divmod(i, 3)
            # Target coordinates
            target_idx = goal.index(state[i])
            goal_row, goal_col = divmod(target_idx, 3)
            distance += abs(curr_row - goal_row) + abs(curr_col - goal_col)
    return distance

def get_neighbors(state):
    neighbors = []
    blank_idx = state.index(0)
    row, col = divmod(blank_idx, 3)
    
    # Possible moves: Up, Down, Left, Right
    moves = [(-1, 0, "UP"), (1, 0, "DOWN"), (0, -1, "LEFT"), (0, 1, "RIGHT")]
    
    for dr, dc, move_name in moves:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            neighbor_idx = r * 3 + c
            new_state = list(state)
            # Swap blank with tile
            new_state[blank_idx], new_state[neighbor_idx] = new_state[neighbor_idx], new_state[blank_idx]
            neighbors.append((tuple(new_state), move_name))
    return neighbors

def solve_8_puzzle(start, goal):
    # Priority Queue stores (f_score, g_score, current_state, path)
    pq = [(get_manhattan_distance(start, goal), 0, start, [])]
    visited = {start: 0}
    step = 0

    while pq:
        f, g, current, path = heapq.heappop(pq)
        
        print(f"\n{'='*60}")
        print(f"STEP {step} | Current f(n): {f} (g={g}, h={get_manhattan_distance(current, goal)})")
        print(f"State: {current[0:3]}\n       {current[3:6]}\n       {current[6:9]}")
        print(f"{'='*60}")

        if current == goal:
            print(f"\nGOAL REACHED in {g} moves!")
            return path

        print("\nEvaluating all possible next states:")
        for neighbor, move_name in get_neighbors(current):
            h = get_manhattan_distance(neighbor, goal)
            new_g = g + 1
            new_f = new_g + h
            
            print(f"  ? Candidate: Move {move_name:<5} -> h(n): {h}, f(n): {new_f}")
            
            if neighbor not in visited or new_g < visited[neighbor]:
                visited[neighbor] = new_g
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [move_name]))
        
        # In A*, the "Selected Move" is the one with the lowest f score in the whole PQ
        # For display purposes, we look at the next item in the PQ
        if pq:
            next_f, next_g, next_state, next_path = pq[0]
            print(f"\n>>> SELECTED NEXT STATE based on lowest f(n)={next_f}")
        
        step += 1

# Configuration
# 0 represents the empty space
START = (2,8,3,1,0,4,7,6,5)
GOAL = (1, 2, 3, 8, 0, 4, 7, 6, 5)

solve_8_puzzle(START, GOAL)