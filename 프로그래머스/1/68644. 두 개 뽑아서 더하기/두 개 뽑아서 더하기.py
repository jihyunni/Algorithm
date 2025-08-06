def solution(numbers):
    answer = []
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            num = numbers[i]+numbers[j] 
            if num not in answer:
                answer.append(num)
                
    return sorted(answer)
