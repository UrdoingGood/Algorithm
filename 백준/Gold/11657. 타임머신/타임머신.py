# 최단거리 - 벨만포드

N, M = map(int, input().split())
arr = []
INF = float('inf')
distance = [INF] * (N+1)

for i in range(M):
    start, end, time = map(int, input().split())
    arr.append((start, end, time))

distance[1] = 0 # 1번 노드는 0으로 초기화

for _ in range(N-1): # 노드가 N개이면 N-1번만 보면 다 볼 수 있음
    for start, end, time in arr:
        if distance[start] != INF and distance[end] > distance[start] + time: # 시작점이 무한대가 아니고,
            distance[end] = distance[start] + time # 새롭게 들어오는 시작점의 노드 + time 보다 더 작은 경우에 갱신

# 음수 사이클 확인
flag = False
for start, end, time in arr:
    if distance[start] != INF and distance[end] > distance[start] + time:
        flag = True

if not flag: # 음수 사이클이 아니라면
    for i in range(2, N+1): # 2번 노드가는 time 부터 출력
        if distance[i] != INF:
            print(distance[i])
        else:  # 그런데 아직도 INF 라면, 해당 노드엔 도달하지 못했다는 뜻이므로 -1 출력
            print(-1)

else:
    print(-1)