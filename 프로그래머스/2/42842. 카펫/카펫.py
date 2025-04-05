def solution(brown, yellow):
    for x in range(brown):
        for y in range(brown):
            if (brown == 2*(x+(y-2))) and (yellow == (x-2)*(y-2)) and (x >= y):
                return [x, y]


