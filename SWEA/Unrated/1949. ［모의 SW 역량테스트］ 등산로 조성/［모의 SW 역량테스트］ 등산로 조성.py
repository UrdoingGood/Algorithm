dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def dfs(cx, cy, length, chk):
    global max_len
    max_len = max(max_len, length)
    visited[cx][cy] = True

    for dx, dy in dxy:
        nx, ny = cx + dx, cy + dy

        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny]:
                continue

            if mountain[cx][cy] > mountain[nx][ny]:
                dfs(nx, ny, length + 1, chk)

            elif not chk and mountain[cx][cy] > mountain[nx][ny] - K:
                origin_len = mountain[nx][ny]
                mountain[nx][ny] = mountain[cx][cy] - 1
                dfs(nx, ny, length + 1, True)
                mountain[nx][ny] = origin_len

    visited[cx][cy] = False

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    max_num = 0
    max_len = 0

    for i in range(N):
        for j in range(N):
            if mountain[i][j] > max_num:
                max_num = mountain[i][j]

    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_num:
                dfs(i, j, 1, False)

    print(f"#{test_case} {max_len}")