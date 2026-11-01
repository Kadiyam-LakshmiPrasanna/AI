import random
Q = {(r,c): [0]*4 for r in range(3) for c in range(3) if (r,c)!=(1,1)}
A = [(1,0),(-1,0),(0,1),(0,-1)]
names = ["Down","Up","Right","Left"]
goal = (2,2)
alpha,gamma,epsilon = 0.5,0.9,0.2
total = 0
for _ in range(100):
    s = (0,0)
    while s != goal:
        a = random.randrange(4) if random.random()<epsilon else Q[s].index(max(Q[s]))
        n = (s[0] + A[a][0],s[1] + A[a][1])
        if n not in Q:
            continue
        reward = 10 if n==goal else -1
        Q[s][a] += alpha*(reward + gamma * max(Q[n])-Q[s][a])
        total += reward
        s = n
print("Q-Table:")
for s,v in Q.items():
    print(s, [round(x,2) for x in v])

print("\nLearned Policy: ")
for s,v in Q.items():
    print(s, names[v.index(max(v))])

print("\nCumulative Reward: ",total)
    
