import random
grid = [[0,0,0],[0,-1,0],[0,0,10]]
actions = [(0,1),(1,0),(0,-1),(-1,0)]
Q = {(r,c):[0.0]*4 for r in range(3) for c in range(3)}

alpha,gamma,epsilon = 0.1,0.9,0.2
start,goal = (0,0),(2,2)

def choose(s):
    return random.randrange(4) if random.random()<epsilon else Q[s].index(max(Q[s]))
rewards = []
for episode in range(100):
    s = start
    a = choose(s)
    total = 0
    while s != goal:
        ns = (s[0] + actions[a][0], s[1] + actions[a][1])
        if ns not in Q:
            ns = s
            r = 0
        else:
            r = grid[ns[0]][ns[1]]
            
        na = choose(ns)
        Q[s][a] += alpha * (r + gamma * Q[ns][na] - Q[s][a])
        total += r
        s,a = ns,na
    rewards.append(total)
print("Learned SARSA Policy: ")
for s,q in Q.items():
    print(s,actions[q.index(max(q))])
print("\nCumulative Reward: ",rewards[-1])
