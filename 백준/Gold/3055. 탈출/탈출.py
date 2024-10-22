from collections import deque

# 물의 위치를 먼저 퍼뜨리고 고슴도치를 이동시키기 위한 함수 분리
def bfs():
    while water_q or hedgehog_q:
        # 물 먼저 확장
        water_size = len(water_q)
        for _ in range(water_size):
            ci, cj = water_q.popleft()
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < R and 0 <= nj < C and graph[ni][nj] == '.':
                    graph[ni][nj] = '*'
                    water_q.append((ni, nj))

        # 고슴도치 이동
        hedgehog_size = len(hedgehog_q)
        for _ in range(hedgehog_size):
            ci, cj = hedgehog_q.popleft()
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < R and 0 <= nj < C:
                    if graph[ni][nj] == 'D':
                        return visited[ci][cj]
                    if graph[ni][nj] == '.':
                        graph[ni][nj] = 'S'
                        visited[ni][nj] = visited[ci][cj] + 1
                        hedgehog_q.append((ni, nj))

    return 'KAKTUS'


R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]

water_q = deque()
hedgehog_q = deque()
visited = [[0] * C for _ in range(R)]

# 비버 집, 고슴도치, 물의 위치 저장
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S':
            hedgehog_q.append((i, j))
            visited[i][j] = 1
        elif graph[i][j] == '*':
            water_q.append((i, j))

result = bfs()
print(result)
