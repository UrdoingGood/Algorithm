from collections import defaultdict

# 시작 노드 번호, 깊이 번호
def dfs(node, depth):
    visited[node] = True

    # 노드별로 깊이 구해주고
    depth_lst[node] = depth
    for child in graph[node]:
        if not visited[child]:
            parent_lst[child] = node
            # 다음 노드(자식 노드)로 갈 때는 깊이 하나 더해서 dfs
            dfs(child, depth + 1)

    # 노드별로 서브트리 개수 더해주기
    subnum_lst[node] = 1 # 처음엔 자기 자신 (1)로 초기화
    for child in graph[node]:
        # 자식 노드의 서브트리 개수 더해주면, 자신의 서브트리 개수가 나옴
        subnum_lst[node] += subnum_lst[child]


# a, b의 공통 조상 찾기
def find_parent(a, b):
    while depth_lst[a] != depth_lst[b]:
        if depth_lst[a] < depth_lst[b]:
            b = parent_lst[b]
        else:
            a = parent_lst[a]

    # 이제 depth가 같아졌으니, 공통 조상을 찾으러 가자
    while a != b:
        a = parent_lst[a]
        b = parent_lst[b]

    return a

T = int(input())
for test_case in range(1, T + 1):
    vcnt, ecnt, a, b = map(int, input().split())
    edges = list(map(int, input().split()))

    # dfs로 순회
    # 부모 노드가 같은지 확인
    # 그 부모 노드까지 몇 개의 노드가 있는지 (서브 트리 개수)

    visited = [False] * (vcnt + 1)
    parent_lst = [0] * (vcnt + 1)
    depth_lst = [0] * (vcnt + 1)
    subnum_lst = [0] * (vcnt + 1)

    graph = defaultdict(list)
    for i in range(ecnt):
        graph[edges[2 * i]].append(edges[2 * i + 1])

    dfs(1, 0)

    print(f"#{test_case} {find_parent(a, b)} {subnum_lst[find_parent(a, b)]}")