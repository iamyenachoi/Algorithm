def solution(spell, dic):
    answer = 0
    for i in dic:
        if set(spell) <= set(i):
            answer = 1
            break
        else:
            answer = 2
    return answer