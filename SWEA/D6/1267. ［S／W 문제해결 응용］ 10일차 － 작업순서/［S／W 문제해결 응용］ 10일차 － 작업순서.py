from collections import defaultdict

# v : 시작 정점
def dfs(v):
    # 현재 정점은 방문했다고 처리
    visited[v] = True

    # 인접한 정점에 대해서 다시 dfs 실행
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor)

    # 여기까지 실행했으면, 가장 안 쪽까지 파고들었다
    # 여기까지 왔다는 건? 이제 인접한 정점이 없다는 뜻
    res.append(v)

for test_case in range(1, 11):
    vcnt, ecnt = map(int, input().split())
    edges = list(map(int, input().split()))

    # 사이클이 없는 방향 그래프 (DAG)
    graph = defaultdict(list)
    for i in range(ecnt):
        graph[edges[2*i]].append(edges[2*i + 1])

    # dfs 방문처리를 위한 방문 리스트 변수
    visited = [False] * (vcnt + 1)
    res = []

    # 모든 정점에 대해 dfs 실행 (방문하지 않은 정점에 대해서만)
    for v in range(1, vcnt + 1):
        if not visited[v]:
            dfs(v)

    print(f"#{test_case}", *(res[::-1]))