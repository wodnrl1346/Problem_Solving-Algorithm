from collections import defaultdict

def solution(nums) -> int: # num: n마리 폰켓몬의 종류 번호가 담긴 배열
    cnt = 0
    freqs = defaultdict(int)
    
    for i in nums:
        freqs[i] += 1
    
    # len(freqs) - 배열에 담긴 폰켓몬의 종류 개수
    # len(nums)/2 - 뽑을 수 있는 폰켓몬의 개수
    
    if len(freqs) >= len(nums)/2:
        cnt = len(nums)/2
    
    elif len(freqs) < len(nums)/2:
        cnt = len(freqs)
    
    return cnt # cnt: n/2 마리의 폰켓폰을 선택하는 방법 중, 가장 많은 종류의 폰캣몬을 선택할 때, 폰켓몬 종류 번호의 개수