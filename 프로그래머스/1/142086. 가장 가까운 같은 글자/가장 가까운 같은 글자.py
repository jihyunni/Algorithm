def solution(s):
    last_index = {}   
    answer = []

    for i, char in enumerate(s):
        if char in last_index:
            answer.append(i - last_index[char])
        else:
            answer.append(-1)
        last_index[char] = i  

    return answer
