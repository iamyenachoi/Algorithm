def solution(array):
    answer = 0
    for i in str(array):
        if str(7) in i:
            answer += 1
    return answer