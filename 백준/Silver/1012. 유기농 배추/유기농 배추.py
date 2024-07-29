T = int(input())

#DFS로 풀었는데 RecursionError 오류발생!!!!
def get_warms(M, N, farm, i, j):
    #종료조건
    global visited
    if i < 0 or i >= M or j < 0 or j >= N: return
    if farm[i][j] == 0: return
    if visited[i][j]: return

    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited[i][j] = True

    for dx, dy in dxy:
        nx = i + dx
        ny = j + dy
        if nx < 0 or nx >= M or ny < 0 or ny >= N: continue
        get_warms(M, N, farm, nx, ny)

for t in range(T):
    M, N, K = map(int, input().split())
    farm = [[0]*N for _ in range(M)]
    for _ in range(K):
        i, j = map(int, input().split())
        farm[i][j] = 1

    warm_cnt = 0
    visited = [[False]*N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if farm[i][j] == 1 and not visited[i][j]:
                get_warms(M, N, farm, i, j)
                warm_cnt += 1
    print(warm_cnt)
