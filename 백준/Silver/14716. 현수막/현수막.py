from collections import deque
def count_char(M, N, board, i, j):
    queue = deque([(i,j)])
    while queue:
        x, y = queue.popleft()
        if x<0 or x>=M or y<0 or y>=N or board[x][y] == 0:
            continue
        board[x][y] = 0
        dxy = [(1,0),(0,1),(-1,0),(0,-1),
           (1,1),(-1,1),(1,-1),(-1,-1)]
        for dx, dy in dxy:
            queue.append((x+dx, y+dy))

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

char_cnt = 0
for i in range(M):
    for j in range(N):
        if board[i][j] == 1:
            char_cnt += 1
            count_char(M, N, board, i, j)
print(char_cnt)