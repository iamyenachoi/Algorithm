def solution(dots):
    answer = 0
    for (i, j, k, l) in [(0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)]:
        if (dots[j][1] - dots[i][1]) * (dots[l][0] - dots[k][0]) == (dots[l][1] - dots[k][1]) * (dots[j][0] - dots[i][0]):
            answer = 1
    return answer