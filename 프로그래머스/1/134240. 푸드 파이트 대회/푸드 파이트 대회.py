def solution(food):
    answer = ''
    
    for i in range(0, len(food)):
        
        # food[0]은 수웅이가 준비한 물의 양이며, 항상 1입니다.
        if i == 0 :
            food[i] = 0
            answer += str(food[i])
            
        # 음식 준비 이상하게 했을 때  
        else:
            fd = food[i]// 2
            answer += str(i) * fd
    
    answer = answer[1:] + answer[0]
    revers = answer[:-1][::-1]
    answer += revers
    return answer