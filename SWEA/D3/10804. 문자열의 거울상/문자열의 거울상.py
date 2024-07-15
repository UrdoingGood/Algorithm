T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    li = list(map(str, input()))
    res = []
    
    for i in reversed(li):
        if i == 'b':
            res.append('d')
        elif i == 'd':
            res.append('b')
        elif i == 'p':
            res.append('q')
        else:
            res.append('p')
            
    print("#{} {}".format(test_case, ''.join(res)))