from collections import deque

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs(i1, j1, i2, j2, count):
    global min_count
    queue = deque()
    queue.append((i1, j1, i2, j2, count))

    while queue:
        ci1, cj1, ci2, cj2, count = queue.popleft()

        if count >= 10:
            return -1

        for dx, dy in dxy:
            ni1, nj1 = dx + ci1, dy + cj1
            ni2, nj2 = dx + ci2, dy + cj2

            out1 = not (0 <= ni1 < N and 0 <= nj1 < M)
            out2 = not (0 <= ni2 < N and 0 <= nj2 < M)

            if out1 and out2:
                continue
            if out1 or out2:
                min_count = min(count + 1, min_count)
                continue

            # 이동하려는 칸이 벽이면, 이동하지 않음
            if not out1 and arr[ni1][nj1] == '#':
                ni1, nj1 = ci1, cj1
            if not out2 and arr[ni2][nj2] == '#':
                ni2, nj2 = ci2, cj2

            queue.append((ni1, nj1, ni2, nj2, count + 1))


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
INF = float('inf')
min_count = INF
coins = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'o':
            coins.append((i, j))

bfs(coins[0][0], coins[0][1], coins[1][0], coins[1][1], 0)

if min_count != INF:
    print(min_count)
else:
    print(-1)