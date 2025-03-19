def solution(babbling):
    answer = 0
    valid = ["aya", "ye", "woo", "ma"]

    for i in babbling:
        temp = i
        for word in valid:
            if word in temp:
                temp = temp.replace(word, " ")
        if temp.strip() == "":
            answer += 1

    return answer