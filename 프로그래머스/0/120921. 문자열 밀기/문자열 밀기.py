def solution(A, B):
    answer = 0
    if A == B:
        answer = 0
    else:
        for i in range(1, len(A) + 1):
            A = A[-1] + A[:-1]
            if A == B:
                answer = i
                break
            else:
                answer = -1
    return answer