def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c[0], c[1], c[2]
        sorted_array = sorted(array[i-1:j])
        answer.append(sorted_array[k-1])
    return answer