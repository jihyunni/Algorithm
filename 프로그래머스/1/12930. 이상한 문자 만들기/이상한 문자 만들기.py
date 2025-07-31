def solution(s):
    answer = ''
    s = s.split(' ')
    
    for idx in range(len(s)):
        word = s[idx]
        for j in range(len(word)):
            if j % 2 == 0:
                answer += word[j].upper()
            else:
                answer += word[j].lower()
        if idx != len(s) - 1:
            answer += ' '
    return answer
