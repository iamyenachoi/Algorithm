def solution(numlist, n):
    temp = []
    for num in numlist:
        temp.append((abs(num - n), num))
    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            if temp[i][0] > temp[j][0] or (temp[i][0] == temp[j][0] and temp[i][1] < temp[j][1]):
                temp[i], temp[j] = temp[j], temp[i]    
    answer = []
    for k in temp:
        answer.append(k[1])    
    return answer