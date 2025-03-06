def solution(num, total):
    answer = []
    middle = total // num
    first = middle - (num // 2)
    if num % 2 == 0:
        first += 1
    for i in range(num):
        answer.append(first + i) 
    return answer