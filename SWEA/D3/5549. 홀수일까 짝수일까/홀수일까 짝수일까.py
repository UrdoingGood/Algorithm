T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = int(input())
    if num % 2 == 0:
        res = "Even"
    else:
        res = "Odd"
    print("#{} {}".format(test_case, res))