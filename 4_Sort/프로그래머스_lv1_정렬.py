def solution(array, commands):
    answer = [] 
    result_arr = []
    for arr in commands:
        i = arr[0]
        j = arr[1]
        k = arr[2]
        
        result_arr = sorted(array[i-1:j])
        answer.append(result_arr[k-1])

    return answer