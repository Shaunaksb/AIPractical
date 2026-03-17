import copy

def calculate_heuristic(stack, goal):
    score = 0
    for i in range(len(stack)):
        if i < len(goal) and stack[i] == goal[i] and stack[:i] == goal[:i]:
            score += i
        else:
            score -= i
    return score

def solve_blocks_world(start, goal):
    current_stack = start[:]
    table = []
    step = 0
    
    print(f"{'='*60}")
    print(f"STARTING STATE | Stack: {current_stack} | Table: {table} | Score: {calculate_heuristic(current_stack, goal)}")
    print(f"{'='*60}")

    # --- PHASE 1: THE SPLIT (Unstacking) ---
    print("\n>>> PHASE 1: DISMANTLING THE STRUCTURE")
    while current_stack:
        current_score = calculate_heuristic(current_stack, goal)
        block_to_move = current_stack[-1]
        
        # In Simple HC, we evaluate the immediate unstacking move
        temp_stack = current_stack[:-1]
        new_score = calculate_heuristic(temp_stack, goal)
        
        print(f"\nSTEP {step} Evaluation:")
        print(f"  ? Candidate: Move {block_to_move} to Table -> Result: {temp_stack} | Score: {new_score}")
        
        # Simple HC takes the move if it's better or neutral (clearing the path)
        if new_score >= current_score or current_score < 0:
            print(f"  >>> SELECTED: Move {block_to_move} to Table")
            table.append(current_stack.pop())
            step += 1
            print(f"  STATE: Stack {current_stack} | Table {table} | Score: {new_score}")
        else:
            break

    # --- PHASE 2: THE MERGE (Building) ---
    print("\n" + "="*60)
    print(">>> PHASE 2: REBUILDING THE GOAL STRUCTURE")
    print("="*60)
    
    while len(current_stack) < len(goal):
        target_block = goal[len(current_stack)]
        current_score = calculate_heuristic(current_stack, goal)
        moved = False
        
        print(f"\nSTEP {step} Evaluation (Looking for {target_block}):")
        
        # Simple HC checks blocks on the table one by one
        for i, block in enumerate(table):
            temp_stack = current_stack + [block]
            new_score = calculate_heuristic(temp_stack, goal)
            
            print(f"  ? Candidate: Move {block} to Stack -> Result: {temp_stack} | Score: {new_score}")
            
            # Simple HC: Take the FIRST move that matches our target goal block
            if block == target_block:
                print(f"  >>> SELECTED: Move {block} from Table to Stack")
                current_stack.append(table.pop(i))
                step += 1
                print(f"  STATE: Stack {current_stack} | Table {table} | Score: {new_score}")
                moved = True
                break
            else:
                print(f"    (Skipped: {block} is not the current target {target_block})")
        
        if not moved:
            print("\nTERMINATED: Target block not found on table.")
            break

    if current_stack == goal:
        print(f"\n{'*'*60}")
        print(f"GOAL REACHED successfully: {current_stack}")
        print(f"{'*'*60}")

# Configuration
START = ['B', 'C', 'D', 'A']
GOAL = ['A', 'B', 'C', 'D']

solve_blocks_world(START, GOAL)