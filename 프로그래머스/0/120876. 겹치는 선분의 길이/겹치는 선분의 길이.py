def solution(lines):
    answer = 0
    a = [0] * 201
    
    for line in lines:
        start, end = line
        start += 100
        end += 100

        for i in range(start, end):
            a[i] += 1

    for i in range(len(a)):
        if a[i] >= 2:
            answer += 1

    return answer
