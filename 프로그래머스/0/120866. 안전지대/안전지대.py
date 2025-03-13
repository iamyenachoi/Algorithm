def solution(board):
    n = len(board)
    danger = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(0)
        danger.append(row)
    
    answer = 0
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        ni = i + di
                        nj = j + dj
                        if 0 <= ni < n and 0 <= nj < n:
                            danger[ni][nj] = 1
    
    for i in range(n):
        for j in range(n):
            if danger[i][j] == 0:
                answer += 1
    
    return answer