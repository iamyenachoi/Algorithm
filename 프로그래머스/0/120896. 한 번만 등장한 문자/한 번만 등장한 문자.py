def solution(s):
    answer = ''
    count = {}
    sorted_s = sorted(s)
    for i in sorted_s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for i in sorted_s:
        if count[i] == 1:
            answer += i
    return answer