def solution(score):
    answer = []
    avg = []
    for i in range(len(score)):
        avg.append((score[i][0] + score[i][1]) / 2)
    for n in range(len(avg)):
        rank = 1
        for j in range(len(avg)):
            if avg[j] > avg[n]:
                rank += 1
        answer.append(rank)
    return answer