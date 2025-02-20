def solution(dots):
    answer = 0
    x_min = dots[0][0]
    x_max = dots[0][0]
    y_min = dots[0][1]
    y_max = dots[0][1]
    for dot in dots:
        x = dot[0]
        y = dot[1]
        if x < x_min:
            x_min = x
        if x > x_max:
            x_max = x
        if y < y_min:
            y_min = y
        if y > y_max:
            y_max = y
    width = x_max - x_min
    height = y_max - y_min
    answer = width * height
    return answer