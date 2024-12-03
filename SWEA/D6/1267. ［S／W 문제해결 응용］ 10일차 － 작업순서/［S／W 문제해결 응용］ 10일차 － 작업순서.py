from collections import defaultdict
from collections import deque


def work():
    queue = deque()
    
    for v in range(1, N):
        if pre[v] == 0:
            queue.append(v)
            
    while queue:
        current = queue.popleft()
        res.append(current)
        
        for child in graph[current]:
            pre[child] -= 1
            if pre[child] == 0:
                queue.append(child)


T = 10
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    edges = list(map(int, input().split()))
    graph = defaultdict(list)
    pre = [0] * (N+1)
    res = []

    for i in range(M):
        a, b = edges[i * 2], edges[i * 2 + 1]
        graph[a].append(b)
        pre[b] += 1

    work()

    print(f"#{test_case}", *res)