def dfs(idx, N, res, plus, minus, mul, div):
    global max_num, min_num

    # 연산자 다 쓰면 끝
    if plus < 0 or minus < 0 or mul < 0 or div < 0:
        return

    # 숫자 다 쓰면 최대, 최소로 각각 갱신
    elif idx == N:
        if max_num < res:
            max_num = res
        if min_num > res:
            min_num = res

    # 연산 진행해주기
    else:
        dfs(idx + 1, N, res + nums[idx], plus - 1, minus, mul, div)
        dfs(idx + 1, N, res - nums[idx], plus, minus - 1, mul, div)
        dfs(idx + 1, N, res * nums[idx], plus, minus, mul - 1, div)
        dfs(idx + 1, N, int(res / nums[idx]), plus, minus, mul, div - 1)

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    plus, minus, mul, div = map(int, input().split())
    nums = list(map(int, input().split()))

    max_num = -100000000
    min_num = 100000000

    dfs(1, N, nums[0], plus, minus, mul, div)

    print(f"#{test_case} {max_num - min_num}")