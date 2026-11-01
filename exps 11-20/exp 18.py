import heapq

graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 2), ("E", 5)],
    "C": [("E", 1)],
    "D": [("G", 3)],
    "E": [("G", 2)],
    "G": []
}

h = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "E": 1,
    "G": 0
}

def a_star(start, goal):
    queue = [(h[start], 0, start, [start])]
    visited = set()
    
    while queue:
        f, cost, node, path = heapq.heappop(queue)        
        if node in visited:
            continue            
        visited.add(node)
        if node == goal:
            return path, cost
        for next_node,edge_cost in (graph[node]):
            if next_node not in visited:
                new_cost = cost + edge_cost
                new_f = new_cost + h[next_node]
                heapq.heappush(queue, (new_f, new_cost, next_node, path + [next_node]))
                
    return None,None

# Test the function
path, cost = a_star("A", "G")
print("Path: ","->".join(path))
print(f"Total Cost: {cost}")

