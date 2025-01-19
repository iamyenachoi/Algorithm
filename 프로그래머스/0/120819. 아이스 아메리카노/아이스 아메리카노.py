def solution(money):
    answer = []
    cups = money // 5500
    change = money - 5500 * cups
    answer = [cups, change]
    return answer