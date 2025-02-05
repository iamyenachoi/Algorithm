def solution(array, n):
    answer = 0
    temp = float('inf')
    array.sort()
    for i in array:
        diff = abs(n - i)
        if diff < temp:
            temp = diff
            answer = i
    return answer
