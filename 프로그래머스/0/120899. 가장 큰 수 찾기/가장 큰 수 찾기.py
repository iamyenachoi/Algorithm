def solution(array):
    answer = []
    n = 0
    for i in range(len(array)):
        if n < array[i]:
            n = array[i]
    answer = [n, array.index(n)]
    return answer