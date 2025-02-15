def solution(sides):
    answer = 0
    a = sides[0]
    b = sides[1]
    for i in range(1, a + b):
        if i + a > b and i + b > a and a + b > i:
            answer += 1
    return answer