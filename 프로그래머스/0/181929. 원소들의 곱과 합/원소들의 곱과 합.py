def solution(num_list):
    answer = 0
    sum_n = 0
    mul_n = 1
    for i in num_list:
        sum_n += i
        mul_n *= i
        if mul_n > sum_n ** 2:
            answer = 0
        elif mul_n < sum_n ** 2:
            answer = 1
    return answer