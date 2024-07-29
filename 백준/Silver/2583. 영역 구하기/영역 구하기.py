import sys
import math
input = sys.stdin.readline

def area_dfs(M, N, graph_paper, visited, i, j):
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    stack = [(i,j)]
    area_size = 0
    while stack:
        x, y = stack.pop()
        if visited[x][y]:
            continue
        visited[x][y] = 1
        area_size += 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and graph_paper[nx][ny] == 0:
                stack.append((nx, ny))
    return area_size

M, N, K = map(int, input().split())
graph_paper = [[0]*N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(M-y2,M-y1):
        for j in range(x1,x2):
            graph_paper[i][j] = 1 #사각형 영역이므로 칠하기

visited = [[0]*N for _ in range(M)]
areas = []
#current_area = 0 # cnt

for i in range(M):
    for j in range(N):
        if graph_paper[i][j] == 0 and visited[i][j] == 0:
            area_size = area_dfs(M, N, graph_paper, visited,i, j)
            areas.append(area_size)

print(len(areas))
areas.sort()
for a in areas:
    print(a, end=' ')