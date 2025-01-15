def solution(s1, s2):
    answer = 0
    for i in s1:
        for n in s2:
            if i == n:
                answer += 1
    return answer