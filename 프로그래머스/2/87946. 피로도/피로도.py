def permutation(arr, n):
    if n == 0:
        return [[]]
    res = []
    for i in range(len(arr)):
        for p in permutation(arr[:i] + arr[i+1:], n-1):
            res.append([arr[i]] + p)
    return res


def solution(k, dungeons):
    all_dungeons = permutation(dungeons, len(dungeons))
    max_cnt = 0
                        
    for dungeon in all_dungeons:
        current_k = k
        cnt = 0
        for i, j in dungeon:
            if current_k >= i:
                current_k -= j
                cnt += 1
            else:
                break
        max_cnt = max(max_cnt, cnt)
        
    return max_cnt