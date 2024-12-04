from collections import defaultdict

dxy = [(), (-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우 1 2 3 4
reverse_direct = [0, 2, 1, 4, 3]

T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(K)]
    new_positions = defaultdict(list)

    for _ in range(M): # 주어진 시간 동안
        new_positions.clear() # 새로운 정보 저장하기 위해서 초기화

        for k in range(len(arr)): # 각 군집들 움직이기
            x, y, micro, direct = arr[k]

            if micro == 0: # 미생물 0마리면 군집 사라짐
                continue

            nx, ny = x + dxy[direct][0], y + dxy[direct][1]

            if 0 <= nx < N and 0 <= ny < N:
                if nx == 0 or nx == N-1 or ny == 0 or ny == N-1:
                    micro = micro // 2
                    direct = reverse_direct[direct]

                new_positions[(nx, ny)].append((micro, direct))

        tmp_arr = [] # 새로운 군집 정보
        for key, group in new_positions.items():
            if len(group) > 1: # 여러 군집 모인 경우
                total_count = sum(x[0] for x in group) # 미생물 합치기

                max_micro = 0
                max_direct = 0
                for micro, direct in group:
                    if micro > max_micro:
                        max_micro = micro
                        max_direct = direct
                # max_micro = max(group, key=lambda x: x[0])[0]
                # max_direct = max(group, key=lambda x: x[0])[1]

                tmp_arr.append((key[0], key[1], total_count, max_direct))
            else:
                tmp_arr.append((key[0], key[1], group[0][0], group[0][1]))

        arr = tmp_arr

    res = sum(micro for _, _, micro, _ in arr)
    print(f"#{test_case} {res}")