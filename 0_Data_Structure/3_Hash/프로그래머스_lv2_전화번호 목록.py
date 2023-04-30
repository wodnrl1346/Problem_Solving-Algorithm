"""1. hash_map"""
def solution(phone_book):
    answer = True
    
    hash_map = {}
    
    for phone_number in phone_book:
        hash_map[phone_number] = 1
        
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
                  
            if temp in hash_map and temp != phone_number:
                return False
    
    return answer


"""2. implementation"""
def solution(phone_book):
    answer = True
    
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break
            
    # 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false
    # 어떤 번호가 다른 번호의 접두어가 경우가 없으면 true    
    return answer