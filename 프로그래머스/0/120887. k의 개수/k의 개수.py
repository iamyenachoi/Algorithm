def solution(i, j, k):
    answer = 0
    for n in range(i, j + 1):
        for digit in str(n):
            if digit == str(k):
                answer += 1
    return answer