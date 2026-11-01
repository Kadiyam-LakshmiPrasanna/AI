def tsp(graph):
    n = len(graph)
    visited = [False] * n
    min_cost = [float('inf')]

    def visit(city,count,cost):
        if count == n:
            total_cost = cost + graph[city][0]
            if total_cost < min_cost[0]:
                min_cost[0] = total_cost
            return
        for next_city in range(n):
            if not visited[next_city] and graph[city][next_city]!=0:
                visited[next_city]=True
                visit(next_city,count+1,cost+graph[city][next_city])
                visited[next_city] = False

    visited[0] = True
    visit(0,1,0)
    return min_cost[0]

graph = [
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
    ]
print("Minimum cost: ",tsp(graph))
