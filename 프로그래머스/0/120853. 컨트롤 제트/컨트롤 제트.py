def solution(s):
    answer = 0
    stack = []
    for i in s.split():
        if i == 'Z':
            if stack:
                stack.pop()
        else:
             stack.append(int(i))
        answer = sum(stack)
    return answer