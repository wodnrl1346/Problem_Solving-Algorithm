from collections import defaultdict

def solution(participant, completion): 
    # participant: 마라톤에 참여한 선수들의 이름이 담긴 배열
    # completion: 완주한 선수들의 이름이 담긴 배열
    
    freqs_part = defaultdict(int) # 존재하지 않는 key의 value가 0의 초기값을 갖는다.   
    freqs_com = defaultdict(int) # 존재하지 않는 key의 value가 0의 초기값을 갖는다.    

    answer = ''
    
    for char in participant:
        freqs_part[char] += 1

    for char in completion:
        freqs_com[char] += 1

    for char in participant:
        if freqs_part[char] != freqs_com[char]:
            answer = char
            
    return answer # 완주하지 못한 선수의 이름