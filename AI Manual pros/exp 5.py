from collections import deque

start = [1, 2, 3, 4, 0, 6, 7, 5, 8]
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

q = deque([(start, [])])
visited = {tuple(start)}

while q:
    s, path = q.popleft()

    if s == goal:
        path.append(s)
        print("Solution found!")
        for step in path:
            print(step[:3])
            print(step[3:6])
            print(step[6:])
            print()
        break

    z = s.index(0)

    for m in [z-3, z+3, z-1, z+1]:
        if 0 <= m < 9 and abs(z//3 - m//3) + abs(z%3 - m%3) == 1:
            n = s.copy()
            n[z], n[m] = n[m], n[z]
            t = tuple(n)

            if t not in visited:
                visited.add(t)
                q.append((n, path + [s]))
