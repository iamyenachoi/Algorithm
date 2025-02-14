def solution(my_string):
    temp = my_string.split()
    answer = int(temp[0])
    for i in range(1, len(temp), 2):
        operator = temp[i]
        number = int(temp[i + 1])
        if operator == '+':
            answer += number
        elif operator == '-':
            answer -= number
    return answer