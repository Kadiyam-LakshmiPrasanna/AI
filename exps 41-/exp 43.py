grid = [
    ['S','.','.','#','.'],
    ['.','#','.','#','.'],
    ['.','.','.','.','.'],
    ['#','.','#','.','.'],
    ['.','.','.','.','G']
    ]
start = (0,0)
goal = (4,4)
actions = {
    'U' : (-1,0),
    'D' : (1,0),
    'L' : (0,-1),
    'R' : (0,1)
    }
rewards = {
    'normal' : -1,
    'obstacle' : -5,
    'goal' : 10
    }
state = start
path = [state]
while state != goal:
    possible = []
    for action,(dr,dc) in actions.items():
        nr,nc = state[0] + dr,state[1] + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            if grid[nr][nc] != '#':
                possible.append((nr,nc))
    next_state = min(
                    possible,
                    key = lambda x:abs(x[0]-goal[0]) + abs(x[1]-goal[1])
        )
    state = next_state
    path.append(state)
print("Grid World: ")
for row in grid:
    print("".join(row))
print("\nPath: ",path)
print("Total steps: ",len(path)-1)
print("Goal Reached: ",state==goal)
