def solution(quiz):
    answer = []
    for i in quiz:
        split_i = i.split()
        if split_i[1] == '+':
            value = int(split_i[0]) + int(split_i[2])
            if str(value) == split_i[4]:
                answer.append("O")
            else:
                answer.append("X")
        elif split_i[1] == '-':
            value = int(split_i[0]) - int(split_i[2])
            if str(value) == split_i[4]:
                answer.append("O")
            else:
                answer.append("X")
    return answer