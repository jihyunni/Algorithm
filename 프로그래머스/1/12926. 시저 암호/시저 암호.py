def solution(s, n):
    answer = ''

    for i in s:
        
        # 공백은 아무리 밀어도 공백입니다. 조건 충족 
        if i == " ":
            answer += " "
            
        elif i.islower():
            answer += chr((ord(i) - ord('a') +n) % 26 + ord('a'))
            
        elif i.isupper():
            answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
        
    return answer