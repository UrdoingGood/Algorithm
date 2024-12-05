def dfs(n, alist, blist):
    global res
    if n == N:
        if len(alist) == len(blist):
            asum = bsum = 0
            for i in range(N//2):
                for j in range(N//2):
                    asum += arr[alist[i]][alist[j]]
                    bsum += arr[blist[i]][blist[j]]
            res = min(res, abs(asum-bsum))
        return
    dfs(n+1, alist+[n], blist)
    dfs(n+1, alist, blist+[n])

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = float('inf')
    dfs(0, [], [])
    print(f"#{test_case} {res}")