from collections import deque

# 맨홀 위치 => 시작점
# 인접 => 이동할 수 있는 파이프
# 만약 내가 2, 0 방향 파이프를 가지고 있으면,
# 0, 2를 가지고 있는 파이프와 연결될 수 있음

# 위, 오른쪽, 아래, 왼쪽
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
pipe = [[], [0, 1, 2, 3], [0, 2], [1, 3], [0, 1], [1, 2], [2, 3], [0, 3]]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    cnt = 1
    while queue:
        cx, cy = queue.popleft()
        current_time = visited[cx][cy]

        if current_time >= L:
            continue

        for i in pipe[tunnel[cx][cy]]:
            nx, ny = cx + dxy[i][0], cy + dxy[i][1]
            if 0 <= nx < N and 0 <= ny < M and tunnel[nx][ny] != 0 and visited[nx][ny] == 0 and (i+2) % 4 in pipe[tunnel[nx][ny]]:
                visited[nx][ny] = current_time + 1
                queue.append((nx, ny))
                cnt += 1

    return cnt

T = int(input())
for test_case in range(1, T + 1):
    # 세로크기, 가로크기, 세로위치, 가로위치, 소요시간
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    print(f"#{test_case} {bfs(R, C)}")