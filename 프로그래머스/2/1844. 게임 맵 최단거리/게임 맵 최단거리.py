from collections import deque

def solution(maps):
    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = True
    
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
               
    while queue:
        cx, cy, count = queue.popleft()
        
        if (cx, cy) == (len(maps)-1, len(maps[0])-1):
            return count
        
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    queue.append((nx, ny, count + 1))
                    visited[nx][ny] = True
    
    return -1