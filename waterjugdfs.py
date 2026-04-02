class Solution:
    def canMeasureWater(self, x, y, target):
        if target > x + y:
            return False

        # Keeping the stack and visited set exactly like your original
        stack = [(0, 0)]
        visited = set()
        step = 0

        print(f"Initial State: x={x}, y={y}, target={target}\n")

        while stack:
            step += 1
            a, b = stack.pop()
            
            # Print current iteration details
            print(f"Step {step}: Current State ({a}, {b}) | Stack Size: {len(stack)}")

            if a + b == target:
                print(f"--> Target {target} found!")
                return True

            if (a, b) in visited:
                print(f"    (State {a, b} already visited, skipping...)")
                continue
            
            visited.add((a, b))

            # Adding moves exactly as you wrote them
            stack.extend([(x, b), (a, y), (0, b), (a, 0)])

            # Pour A into B
            w_ab = min(a, y - b)
            stack.append((a - w_ab, b + w_ab))

            # Pour B into A
            w_ba = min(b, x - a)
            stack.append((a + w_ba, b - w_ba))

        print("--> Target not reachable.")
        return False

# Standalone execution
if __name__ == "__main__":
    sol = Solution()
    # Using small numbers so the output is easy to read
    sol.canMeasureWater(3, 5, 4)