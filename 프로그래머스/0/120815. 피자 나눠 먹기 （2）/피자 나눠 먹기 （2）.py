def solution(n):
    answer = 0
    a, b = 6, n
    while b != 0:
        a, b = b, a % b
    answer = (6 * n) // a // 6
    return answer