def solution(s):
    last_index = {}     # 각 문자의 마지막 등장 인덱스 기록
    answer = []

    for i, char in enumerate(s):
        if char in last_index:
            answer.append(i - last_index[char])
        else:
            answer.append(-1)
        last_index[char] = i  # 현재 위치로 갱신

    return answer
