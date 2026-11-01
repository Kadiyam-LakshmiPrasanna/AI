from collections import deque
graph = {
    "A" : ["B","C"],
    "B" : ["D","E"],
    "C" : ["F"],
    "D" : ["G"],
    "E" : ["G"],
    "F" : ["G"],
    "G" : []
    }

def dfs_recursive(node,visited):
    visited.add(node)
    print(node,end = " ")

    for next_node in graph[node]:
        if next_node not in visited:
            dfs_recursive(next_node,visited)

print("Recursive DFS:")
dfs_recursive("A",set())

def iterative_dfs(start):
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node,end=" ")

            for next_node in reversed(graph[node]):
                if next_node not in visited:
                    stack.append(next_node)

print("\nIterative DFS: ")
iterative_dfs("A")
