print("DFS: ")
def dfs(node,visited):
    print(f"visiting: {node}")
    visited.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(neighbour,visited)
    print(f"backtracking from: {node}")

graph = {
    'A' : ['B','C'],
    'B' : ['A'],
    'C' : []
    }
visited = set()
dfs('A',visited)

print("BFS: ")
def bfs(graph,start):
    queue = [start]
    visited = []
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node,end = ' ')
            visited.append(node)
            queue.extend(graph[node])

graph = {
    'A' : ['D','B'],
    'B' : ['C'],
    'C' : ['E'],
    'D' : [],
    'E' : []
    }
bfs(graph,'A')
