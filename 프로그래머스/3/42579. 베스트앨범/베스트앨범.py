from collections import defaultdict
def solution(genres, plays):
    top = defaultdict(list)
    count = defaultdict(int)
    for i in range(len(genres)):
        top[genres[i]].append((i, plays[i]))
        count[genres[i]] += plays[i]
    
    sorted_genres = sorted(count, key=count.get, reverse=True)
    
    res = []
    for genre in sorted_genres:
        sorted_songs = sorted(top[genre], key=lambda x: (-x[1], x[0]))
        res += [idx for idx, _ in sorted_songs[:2]]
    
    return res