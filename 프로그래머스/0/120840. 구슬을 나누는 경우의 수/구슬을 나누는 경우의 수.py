def solution(balls, share):
    answer = 0
    temp1 = 1
    temp2 = 1
    temp3 = 1
    for i in range(2, (balls - share) + 1):
        temp1 *= i
    for j in range(2, share + 1):
        temp2 *= j
    for k in range(2, balls + 1):
        temp3 *= k
    answer = temp3 / (temp1 * temp2)
    return answer