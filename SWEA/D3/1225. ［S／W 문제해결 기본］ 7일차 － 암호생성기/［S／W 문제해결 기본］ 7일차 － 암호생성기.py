T = 10
for test_case in range(1, T + 1):
    tc = int(input())
    queue = list(map(int, input().split()))
    i = 1
    while True:
        if i > 5: # i가 1~5 사이에 있도록 함
            i = 1
        q = queue.pop(0) - i # 첫 번째 원소를 pop해서 i 만큼 빼기
        if q <= 0: # 만약 뺀 값이 0보다 작거나 같으면
            queue.append(0) # 0을 맨 뒤에 추가
            break # 0이면 끝나므로 break로 나가기
        queue.append(q) # 뺀 값이 0보다 크면 그 값을 맨 뒤에 추가
        i += 1
    print(f"#{test_case}", *queue)
    
'''
# 강사님 풀이
for _ in range(10):
	tc = int(input())
    input_list = list(map(int, input().split()))
    pw_queue = collections.deque(input_list)
    
    reduce_cnt = 1
    
    while True:
    	if reduce_cnt > 5:
        	reduce_cnt = 1
        
        pop_num = pw_queue.popleft() - reduce_cnt
        if pop_num <= 0:
        	pw_queue.append(0)
            break
        pw_queue.append(pop_num)
        reduce_cnt += 1
'''