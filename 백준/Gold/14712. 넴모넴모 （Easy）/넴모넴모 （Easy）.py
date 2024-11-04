N, M = map(int, input().split())
arr = [[0] * M for _ in range(N)]

def dfs(cnt):
    global res
    m = cnt // M
    n = cnt % M

    # cnt가 N * M이면 마지막 블록에 도달했다는 뜻
    if cnt == N * M:
        res += 1
        return # 개수 추가하고 끝

    dfs(cnt + 1)
    # 해당 위치 주변의 세 블럭 중 하나라도 비어 있으면 넴모넴모가 되지 않으므로
    if arr[m][n-1] == 0 or arr[m-1][n] == 0 or arr[m-1][n-1] == 0:
        arr[m][n] = 1 # 해당 위치에 블럭을 놓을 수 있음
        dfs(cnt + 1) # 다음 위치에서도 계속 진행
        arr[m][n] = 0 # 복구 해주기

res = 0
dfs(0)
print(res)