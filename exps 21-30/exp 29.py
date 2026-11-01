import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 2)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

h = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 2, 'G': 0}

def search(start, goal, method):
    frontier = [(0, start, [start])]
    visited = set()

    while frontier:
        cost, node, path = heapq.heappop(frontier)

        if node == goal:
            print(method, "Path:", path, "Cost:", cost)
            return

        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                if method == "BFS":
                    priority = len(path)
                elif method == "DFS":
                    priority = -len(path)
                elif method == "UCS":
                    priority = cost + weight
                elif method == "Greedy":
                    priority = h[neighbor]
                else:
                    priority = cost + weight + h[neighbor]

                heapq.heappush(
                    frontier,
                    (priority, neighbor, path + [neighbor])
                )

for algorithm in ["BFS", "DFS", "UCS", "Greedy", "A*"]:
    search("A", "G", algorithm)
