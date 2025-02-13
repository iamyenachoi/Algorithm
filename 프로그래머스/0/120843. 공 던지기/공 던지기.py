def solution(numbers, k):
    answer = 0
    index = 0
    for i in range(k - 1):
        index += 2
        if index >= len(numbers):
            index -= len(numbers)
    answer = numbers[index]
    return answer