vowels = ['A', 'E', 'I', 'O', 'U']
count = 0
found = False

def dfs(current, word):
    global count, found
    if found == True:
        return
    if current == word:
        found = True
        return
    count += 1
    if len(current) == 5:
        return
    for v in vowels:
        dfs(current+v, word)

def solution(word):
    global count
    dfs("", word)
    return count