def decode(code, dic):
    realcode = []
    for i in range(0, len(code), 7):
        segment = ''.join(map(str, code[i:i+7]))
        for key, value in dic.items():
            if segment == value:
                realcode.append(key)
                break
    return realcode

def valid(code):
    odd_sum = sum(code[i] for i in range(0, len(code), 2))
    even_sum = sum(code[i] for i in range(1, len(code), 2))
    check_sum = (odd_sum * 3) + even_sum
    return check_sum % 10 == 0

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [ list(map(int, input())) * M for _ in range(N) ]
    row, col = 0, 0
    dic = {0:'0001101', 1:'0011001', 2:'0010011', 3:'0111101', 4:'0100011', 5:'0110001', 6:'0101111', 7:'0111011', 8:'0110111', 9:'0001011'}
    
    for i in range(N-1, 0, -1):
        for j in range(M-1, 0, -1):
            if arr[i][j] == 1:
                row = i
                col = j
                break
    code = arr[row][col-55:col+1]
    realcode = decode(code, dic)
    
    if valid(realcode):
        res = sum(realcode)
    else:
        res = 0
    print(f"#{test_case} {res}")