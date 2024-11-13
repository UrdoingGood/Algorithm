from collections import defaultdict
from collections import deque

def dfs(current):
    visited[current] = True
    res_dfs.append(current)
    for next in arr[current]:
        if not visited[next]:
            dfs(next)

def bfs(current):
    queue = deque()
    visited[current] = True
    res_bfs.append(current)
    queue.append(current)
    while queue:
        current = queue.popleft()
        for next in arr[current]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                res_bfs.append(next)

N, M, V = map(int, input().split())
arr = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, N + 1):
    arr[i].sort()

visited = [False] * (N + 1)
res_dfs = []
dfs(V)

visited = [False] * (N + 1)
res_bfs = []
bfs(V)

print(*res_dfs)
print(*res_bfs)