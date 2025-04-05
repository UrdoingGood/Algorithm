# 모든 순열 만들기
# 0이 앞에 오는 경우도 있으니 10진수로 다시 변환 int()
# 소수가 아닌 숫자는 제거, len 계산

def permutation(arr, n):
    if n == 0:
        return [[]]
    res = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for perm in permutation(rest, n-1):
            res.append([arr[i]] + perm)
    return res


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    unique_numbers = set()
    
    for i in range(1, len(numbers)+1):
        perms = permutation(numbers, i)
        for p in perms:
            num = int(''.join(p))
            unique_numbers.add(num)
            
    answer = sum(1 for num in unique_numbers if is_prime(num))
    return answer