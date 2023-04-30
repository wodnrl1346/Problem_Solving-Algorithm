def solution(s):
    answer = True
    stack = []
    
    for char in s:        
        # 1. (일 때
        if char == '(':
            stack.append(char)
        
        # 2. )일 때
        elif char == ')':
            if not stack: # 열려있는 괄호가 없을 때 ')'가 들어오면
                return False
            
            else: # 열려있는 괄호가 있으면 '(' pop
                stack.pop()
    
    answer = False if stack else True
    
    return answer