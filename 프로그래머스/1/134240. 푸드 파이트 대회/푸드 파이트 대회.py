def solution(food):
    answer = ''
    
    for i in range(0, len(food)):
        
        # 조건: food[0]은 수웅이가 준비한 물의 양이며, 항상 1입니다.
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

---------------------------------------------------------------------------
## GPT씨의 내 코드 보완 ##
def solution(food):
    answer = ''
    
    for i in range(0, len(food)):
        if i == 0:
            continue  # 굳이 0을 넣었다 뺐다 하지 말고 skip
        else:
            fd = food[i] // 2
            answer += str(i) * fd

    revers = answer[::-1]
    return answer + '0' + revers
