def solution(sizes):
    answer = 0
    row = []
    col = []
    
    for j in sizes:
        row.append(j[0])
        col.append(j[1])
    
    for i in range(0, len(row)):
        if row[i] < col[i]:
            row[i], col[i] = col[i], row[i]
        else: 
            row[i], col[i] = row[i], col[i]
    
    answer = max(row) * max(col)
    
        
    return answer