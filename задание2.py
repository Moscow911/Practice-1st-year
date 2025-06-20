def dfs(g, graph, visited):
    visited[g] = True
    for v in graph[g]:
        if not visited[v]:
            dfs(v, graph, visited)

def res():
    N, M = map(int, input().split())

    graph = {i: [] for i in range(1, N + 1)}
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (N + 1)
    comp = 0

    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i, graph, visited)
            comp += 1      
    print(comp - 1)

if __name__ == "__main__":
    res()
