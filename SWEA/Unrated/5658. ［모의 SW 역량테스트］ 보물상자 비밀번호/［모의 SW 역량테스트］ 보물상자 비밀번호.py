T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    password = input()

    res = set()
    cnt = N // 4
    password += password[:cnt]

    for i in range(cnt):
        # for j in range(4):
        #     res.add(password[i+j*cnt:i+j*cnt+cnt])
        for j in range(i, N+cnt, cnt):
            res.add(password[j:j+cnt])

    ans = []
    for r in res:
        ans.append(int(r, 16))
    ans.sort(reverse=True)

    print(f"#{test_case} {ans[K-1]}")