def calculate_heuristic(stack, goal):
    score = 0
    for i in range(len(stack)):
        # If block and its support match goal: +length of support
        if i < len(goal) and stack[i] == goal[i] and stack[:i] == goal[:i]:
            score += i
        else:
            # Wrong block or wrong support: -length of support
            score -= i
    return score

def solve_blocks_world(start, goal):
    current_stack = start[:]
    table = []
    step = 0
    
    print(f"Step {step}: Stack {current_stack} | Table {table} | Score: {calculate_heuristic(current_stack, goal)}")

    # --- PHASE 1: THE SPLIT ---
    # We dismantle as long as the stack isn't empty.
    # Simple Hill Climbing: Each removal improves score or stays at 0.
    while current_stack:
        block = current_stack.pop()
        table.append(block)
        step += 1
        print(f"Step {step}: Stack {current_stack} | Table {table} | Score: {calculate_heuristic(current_stack, goal)}")

    # --- PHASE 2: THE MERGE ---
    # We look at the table and only pick up the block that matches the next goal position.
    while len(current_stack) < len(goal):
        moved = False
        target_block = goal[len(current_stack)]
        
        if target_block in table:
            table.remove(target_block)
            current_stack.append(target_block)
            moved = True
            step += 1
            print(f"Step {step}: Stack {current_stack} | Table {table} | Score: {calculate_heuristic(current_stack, goal)}")
        
        if not moved:
            print("Stuck! Target block not on table.")
            break

    if current_stack == goal:
        print("\nGoal Reached successfully!")

# Configuration
START = ['B', 'C', 'D', 'A']
GOAL = ['A', 'B', 'C', 'D']

solve_blocks_world(START, GOAL)