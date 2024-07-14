def find_min_diff(height, N, B):
    tower_min = [float('inf')]
 
    def dfs(index, current_height):
        if current_height >= B:
            tower_min[0] = min(tower_min[0], current_height - B)
            return
        if index == N:
            return
        # 현재 점원을 포함하지 않는 경우
        dfs(index + 1, current_height)
        # 현재 점원을 포함하는 경우
        dfs(index + 1, current_height + height[index])
 
    dfs(0, 0)
    return tower_min[0]
 
T = int(input())
# 여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
 
    res = find_min_diff(height, N, B)
     
    print("#{} {}".format(test_case, res))
