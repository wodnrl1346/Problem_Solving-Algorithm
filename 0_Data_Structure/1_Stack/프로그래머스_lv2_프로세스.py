from collections import deque

def solution(priorities, location):
    # priorities: 프로세스의 중요도가 순서대로 담긴 배열
    # location: 몇 번째로 실행되는 지 알고싶은 프로세스의 위치를 알려준다
    answer = 0
    index = deque()
    
    for i in range(0, len(priorities)):
        index.append(i)

    result = []
    result_index = []
    
    while True:    
        pre = priorities.pop(0)
        pre_index = index.popleft()
        if not priorities:
            result.append(pre)
            result_index.append(pre_index)
            break
        
        if pre < max(priorities):
            priorities.append(pre)
            index.append(pre_index)
                        
        else:
            result.append(pre)
            result_index.append(pre_index)
            
    answer = result_index.index(location) + 1
    return answer