from collections import defaultdict, deque

def bfs():
    queue = deque()
    for v in range(1, N+1):
        if pre[v] == 0:
            queue.append(v)
            res[v] = 1
    while queue:
        current = queue.popleft()
        for node in graph[current]:
            pre[node] -= 1
            if pre[node] == 0:
                queue.append(node)
                res[node] = res[current] + 1

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
graph = defaultdict(list)
pre = [0] * (N+1)
res = [0] * (N+1)

for a, b in edges:
    graph[a].append(b)
    pre[b] += 1

bfs()

print(*res[1:])