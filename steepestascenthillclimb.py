import copy

def calculate_global_heuristic(state, goal_stack):
    total_score = 0
    for stack in state:
        for i, block in enumerate(stack):
            current_support = stack[:i]
            goal_idx = goal_stack.index(block)
            goal_support = goal_stack[:goal_idx]
            
            if current_support == goal_support:
                total_score += len(current_support)
            else:
                total_score -= len(current_support)
    return total_score

def solve_steepest_ascent(start_blocks, goal_stack):
    state = [start_blocks]
    step = 0
    
    while True:
        current_score = calculate_global_heuristic(state, goal_stack)
        print(f"\n--- STEP {step} ---")
        print(f"Current State: {state} | Current Score: {current_score}")
        
        candidates = []
        # Generate all possible moves
        for i, stack_from in enumerate(state):
            for j in range(len(state) + 1):
                if i == j: continue
                
                temp_state = copy.deepcopy(state)
                block = temp_state[i].pop()
                if j < len(state):
                    temp_state[j].append(block)
                else:
                    temp_state.append([block])
                
                temp_state = [s for s in temp_state if s]
                score = calculate_global_heuristic(temp_state, goal_stack)
                candidates.append((score, temp_state, block, i, j))

        # Show all intermediate evaluations
        print("Evaluating possible moves:")
        for score, s, block, fr, to in candidates:
            dest = f"Stack {to}" if to < len(state) else "Table"
            print(f"  > Move {block} from Stack {fr} to {dest} -> Score: {score}")

        # Selection logic
        candidates.sort(key=lambda x: x[0], reverse=True)
        best_score, best_state, b_name, b_fr, b_to = candidates[0]

        if best_score > current_score:
            state = best_state
            step += 1
            dest_name = f"Stack {b_to}" if b_to < len(state) else "Table"
            print(f"SELECTED MOVE: {b_name} to {dest_name} with Score {best_score}")
            
            if len(state) == 1 and state[0] == goal_stack:
                print(f"\nFINAL STATE REACHED: {state} | Score: {best_score}")
                break
        else:
            print("\nTERMINATED: No move improves the current score.")
            break

START = ['B', 'C', 'D', 'A']
GOAL = ['A', 'B', 'C', 'D']
solve_steepest_ascent(START, GOAL)