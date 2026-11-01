from itertools import permutations

cost = [[0,10,15,20],
        [10,0,35,25],
        [15,35,0,30],
        [20,25,30,0]]

def distance(p):
    return sum(cost[p[i]p[i+1]] for i in range(3))+ cost[p[3]][p[0]]

paths = [[0]+list(p) for p in permutations([1,2,3])]
best = min(paths,key=distance)
print("Brute Force: ",best,distance(best))

path = [0]
while len(path) < 4:
    nxt = min(i for i in range(4) if i not in path),
          key = lambda i:cost[path[-1]][i])
          path.append(nxt)

print("Nearest neighbor: ",path,distance(path))

path = best[:]
print("Local Search: ",path,distance(path))
