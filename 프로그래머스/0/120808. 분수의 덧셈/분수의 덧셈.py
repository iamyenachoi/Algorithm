def solution(numer1, denom1, numer2, denom2):
    answer = []
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    a, b = numer, denom
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    answer = numer // a, denom // a
    return answer