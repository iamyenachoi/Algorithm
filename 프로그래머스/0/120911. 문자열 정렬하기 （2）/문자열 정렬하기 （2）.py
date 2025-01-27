def solution(my_string):
    answer = ''
    lower = []
    for i in my_string:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            lower.append(chr(ord(i) + 32))
        else:
            lower.append(i)
    answer = ''.join(sorted(lower))
    return answer