from collections import defaultdict
from collections import deque

def bfs(start, graph, n):
    queue = deque([start])
    visited = [False] * (n+1)
    visited[start] = True
    count = 1
    
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
                
    return count
    

def solution(n, wires):
    min_diff = float('inf')
    
    for i in range(len(wires)):
        temp = wires[:i] + wires[i+1:]
        graph = [[] for _ in range(n+1)]
        
        for a, b in temp:
            graph[a].append(b)
            graph[b].append(a)
            
        count = bfs(1, graph, n)
        diff = abs(n - count - count)
        min_diff = min(min_diff, diff)
        
    return min_diff