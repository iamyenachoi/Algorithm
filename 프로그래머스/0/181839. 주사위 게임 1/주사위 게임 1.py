def solution(a, b):
    answer = 0
    if a % 2 != 0 and b % 2 != 0:
        answer = a ** 2 + b ** 2
    elif a % 2 == 1 or b % 2 == 1:
        answer = 2 * (a + b)
    else:
        answer = a - b
        if answer < 0:
            answer *= -1
    return answer