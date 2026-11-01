import heapq
import time
import tracemalloc

graph = {
    'A' : [('B',1),('C',4)],
    'B' : [('D',2),('E',5)],
    'C' : [('F',2)],
    'D' : [('G',3)],
    'E' : [('G',1)],
    'F' : [('G',2)],
    'G' : []
    }
h = {'A':5,'B':4,'C':3,'D':2,'E':1,'F':2,'G':0}

def search(start,goal,method):
    frontier = [(0,start,[start])]
    visited = set()
    expanded = 0

    while frontier:
        cost,node,path = heapq.heappop(frontier)

        if node in visited:
            continue
        visited.add(node)
        expanded += 1

        if node == goal:
            return expanded,cost

        for neighbor,weight in graph[node]:
            if neighbor not in visited:
                new_cost = cost+weight

                if method == "BFS":
                    priority = len(path)
                elif method == "DFS":
                    priority = -len(path)
                elif method == "UCS":
                    priority = new_cost
                elif method == "Greedy":
                    priority = h[neighbor]
                else:
                    priority = new_cost + h[neighbor]

                heapq.heappush(
                    frontier,
                    (priority, neighbor, path + [neighbor])
                )

for method in ["BFS","DFS","UCS","Greedy","A*"]:
    tracemalloc.start()
    start_time = time.perf_counter()

    expanded,cost = search("A","G",method)

    elapsed = time.perf_counter()-start_time
    _,memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(method,"Nodes Expanded: ",expanded,
          "Time: ",round(elapsed,6),"seconds",
          "Memory: ",memory,"bytes",
          "Path Cost: ",cost)
                    











        
    
