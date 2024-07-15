T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    li = [list(map(int, input())) for _ in range(N)]
    res = 0
    start = N//2
    end = N//2 + 1
    for i in range(N):
        if i < N//2:
            for j in range(start, end):
                res += li[i][j]
            start -= 1
            end += 1
        else:
            for j in range(start, end):
                res += li[i][j]
            start += 1
            end -= 1
    print("#{} {}".format(test_case, res))