from collections import deque

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(i, j):
    spore_cnt = 1
    queue = deque()
    queue.append((i, j))
    arr[i][j] = 1 # 버섯 심기
    while queue:
        ci, cj = queue.popleft()
        for dx, dy in dxy:
            ni, nj = ci + dx, cj + dy
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                # 어떤 모양으로 퍼지든 일단 개수가 중요
                queue.append((ni, nj))
                arr[ni][nj] = 1  # 버섯 심기
                spore_cnt += 1
                if spore_cnt == K:
                    return


def mushroom():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt += 1
    
    # 버섯 포자를 하나 이상 꼭 사용해야함 !!!
    # 이 조건을 안 넣었더니 틀렸다고 떴음
    if cnt == 0:
        print('IMPOSSIBLE')
        return

    if M < cnt:
        print('IMPOSSIBLE')
        return

    if K == 1:
        print('POSSIBLE')
        print(M - cnt)
        return

    spore_used = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                bfs(i, j)
                spore_used += 1
                if spore_used > M:
                    print('IMPOSSIBLE')
                    return

    print('POSSIBLE')
    print(M - spore_used)


mushroom()