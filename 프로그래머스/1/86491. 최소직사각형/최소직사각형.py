def solution(sizes):
    x = []
    y = []
    for card in sizes:
        card.sort()
        x.append(card[0])
        y.append(card[1])
    x.sort()
    y.sort()
    return x[-1] * y[-1]