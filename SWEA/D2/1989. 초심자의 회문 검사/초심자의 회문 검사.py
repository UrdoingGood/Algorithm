def func(word):
    if len(word) <= 1:
        return 1
    if word[0] != word[-1]:
        return 0
    return func(word[1:-1])
        
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    word = list(input())
    res = func(word)
    print(f"#{test_case} {res}")