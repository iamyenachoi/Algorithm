def solution(common):
    answer = 0
    diff = common[1] - common[0]
    if common[1] - common[0] == diff and common[2] - common[1] == diff:
        answer = common[-1] + diff
    else:
        ratio = common[1] // common[0]
        if common[1] % common[0] == 0 and common[2] // common[1] == ratio:
            answer = common[-1] * ratio
    return answer