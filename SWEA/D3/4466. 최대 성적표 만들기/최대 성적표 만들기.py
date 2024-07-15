T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    res = 0
    score = list(map(int, input().split()))
    score.sort(reverse=True)
    for k in range(K):
        res += score[k]
    print("#{} {}".format(test_case, res))