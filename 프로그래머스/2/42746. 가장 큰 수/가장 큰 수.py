def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse=True)
    # 문자열 정렬이라서 303030보다 333이 더 큰 것으로 간주됨
    # 따라서 정렬하면 3, 30 순으로 오게 되는 것임
    res = ''.join(numbers)
    return str(int(res))


# # 시간초과 남
# def permutation(arr, n):
#     res = []
#     if n == 0:
#         return [[]]
#     for i, elem in enumerate(arr):
#         for p in permutation(arr[:i]+arr[i+1:], n-1):
#             res.append(str(elem) + ''.join(map(str, p)))
#     return res

# def solution(numbers):
#     res = permutation(numbers, len(numbers))
#     res.sort()
#     return res[-1]