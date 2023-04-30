from collections import deque
from math import ceil
from collections import Counter

def solution(progresses, speeds):
    # progresses: 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열
    # speeeds: 각 작업의 개발 속도가 적힌 정수 배열 
    answer = []
    q = deque()
    
    for i in range(len(progresses)):
        q.append(ceil((100-progresses[i])/speeds[i]))
    
    q1 = []

    for i in range(len(progresses)-1):
        if q[i] > q[i+1]:
            q[i+1] = q[i]
        
    answer = list(Counter(q).values())
    return answer # 각 배포마다 몇개의 기능이 배포되는지