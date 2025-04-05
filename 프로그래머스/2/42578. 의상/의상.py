from collections import defaultdict

def solution(clothes):
    clist = defaultdict(int)
    for cloth in clothes:
        clist[cloth[1]] += 1
    answer = 1
    for val in clist.values():
        answer *= val + 1
        
    return answer - 1