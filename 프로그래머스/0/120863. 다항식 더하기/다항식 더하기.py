def solution(polynomial):
    answer = ''
    term_x = 0
    term_constant = 0
    split_p = polynomial.split()
    
    for i in range(len(split_p)):
        if 'x' in split_p[i]:
            if split_p[i] == 'x':
                term_x += 1
            elif split_p[i] == '-x':
                term_x -= 1
            else:
                num = split_p[i][:-1]
                term_x += int(num)
        elif split_p[i] not in ('+', '-'):
            term_constant += int(split_p[i])
    
    if term_x == 0 and term_constant == 0:
        return '0'
    
    if term_x != 0:
        if term_x == 1:
            answer += 'x'
        elif term_x == -1:
            answer += '-x'
        else:
            answer += str(term_x) + 'x'
    
    if term_constant != 0:
        if term_x != 0:
            answer += ' + ' + str(term_constant)
        else:
            answer += str(term_constant)
    
    return answer
