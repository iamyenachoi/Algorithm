def solution(my_string):
    answer = ''
    s = set()
    for i in my_string:
        if i not in s:
            answer += i
            s.add(i)
    return answer