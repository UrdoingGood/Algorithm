from collections import defaultdict
from collections import deque

def bfs():
    global semester

    queue = deque()
    for v in range(1, N+1):
        if pre[v] == 0:
            queue.append(v)
            semester[v] = 1

    while queue:
        current = queue.popleft()
        for post in graph[current]:
            pre[post] -= 1 # 선수 과목 하나 들었으니까 1 빼주기
            if pre[post] == 0: # 선수 과목 다 들었으면
                queue.append(post) # 큐에 넣어주기
                semester[post] = semester[current] + 1 # 학기 수 추가


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

pre = [0] * (N + 1) # 선수 과목 개수
semester = [0] * (N + 1) # 학기 수

graph = defaultdict(list)
for a, b in edges:
    graph[a].append(b)
    pre[b] += 1 # 선수 과목 개수 추가

bfs()

print(*semester[1:])