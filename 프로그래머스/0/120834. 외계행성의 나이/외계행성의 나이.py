def solution(age):
    answer = ''
    alphabet = 'abcdefghij'
    while age > 0:
        answer = alphabet[age % 10] + answer
        age = age // 10
    return answer