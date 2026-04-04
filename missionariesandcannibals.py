def missionaries_cannibals():
    # (missionaries on left, cannibals on left, boat side 1=left 0=right)
    start = (3, 3, 1)
    goal  = (0, 0, 0)
    queue = [(start, [start])]
    visited = []

    def valid(m, c):
        if m < 0 or c < 0 or m > 3 or c > 3:
            return False
        if m > 0 and m < c:
            return False
        if (3-m) > 0 and (3-m) < (3-c):
            return False
        return True

    while queue:
        (m, c, b), path = queue.pop(0)
        if (m, c, b) in visited:
            continue
        visited.append((m, c, b))

        if (m, c, b) == goal:
            print("Solution:")
            for s in path:
                print(f"Left -> {s[0]}M {s[1]}C | Right -> {3-s[0]}M {3-s[1]}C | Boat={'Left' if s[2] else 'Right'}")
            return

        for dm, dc in [(1,0),(2,0),(0,1),(0,2),(1,1)]:
            if b == 1:
                nm, nc, nb = m-dm, c-dc, 0
            else:
                nm, nc, nb = m+dm, c+dc, 1
            if valid(nm, nc):
                queue.append(((nm, nc, nb), path + [(nm, nc, nb)]))

missionaries_cannibals()