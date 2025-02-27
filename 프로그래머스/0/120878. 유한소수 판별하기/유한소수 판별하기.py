def solution(a, b):
    answer = 0
    if len(str(a / b)) < 15:
        answer = 1
    else:
        answer = 2
    return answer