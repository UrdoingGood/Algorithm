import itertools

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = float('INF')

    num_list = [i for i in range(N)]

    all_food = itertools.combinations(num_list, N//2)
    for a_food in all_food:
        b_food = []

        for num in num_list:
            if num not in a_food:
                b_food.append(num)

        a_sy_list = itertools.combinations(a_food, 2)
        a_sy_sum = 0
        for a_sy in a_sy_list:
            i, j = a_sy
            a_sy_sum += (arr[i][j] + arr[j][i])

        b_sy_list = itertools.combinations(b_food, 2)
        b_sy_sum = 0
        for b_sy in b_sy_list:
            i, j = b_sy
            b_sy_sum += (arr[i][j] + arr[j][i])

        res = min(res, abs(a_sy_sum - b_sy_sum))

    print(f"#{test_case} {res}")