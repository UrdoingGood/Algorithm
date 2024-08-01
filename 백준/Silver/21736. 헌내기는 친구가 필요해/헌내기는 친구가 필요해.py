from collections import deque

N, M = map(int, input().split())
campus = [list(input()) for _ in range(N)]

def find_friends_bfs(i, j, campus, n, m):
    global result
    queue = deque([(i, j)])
    while queue:
        x, y = queue.popleft()
        #경계이거나, 벽이거나
        #친구면 -> result += 1
        if x < 0 or x >= n or y < 0 or y >= m or campus[x][y] == 'X' or campus[x][y] == 'D':
            continue
        if campus[x][y] == 'P':
            result += 1
            campus[x][y] = 'D'
        campus[x][y] = 'D'
        dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            queue.append((nx, ny))

start_i = 0
start_j = 0
result = 0

for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
           start_i = i
           start_j = j

find_friends_bfs(start_i, start_j, campus, N, M)
print(result if result != 0 else 'TT')