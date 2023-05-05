from collections import defaultdict

def solution(clothes):
    #서로 다른 옷의 조합 수    
    wear = defaultdict(list)
    
    # 모든 경우를 다 구할 필요없이, 경우의 수만을 구하면 된다.
    for [a, b] in clothes:
        wear[b].append(a)
    
    cnt = 1
    for i in wear:
        cnt *= len(wear[i])+1
    
    answer = cnt - 1
    return answer