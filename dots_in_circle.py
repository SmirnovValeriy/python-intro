from math import sqrt


def dist(x_0, y_0, x_1, y_1):
    return sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)


answer = 'YES'
x_c, y_c, r = [int(s) for s in input().split(',')]
x, y = [int(s) for s in input().split(',')]
while dist(x, y, 0, 0) > 0:
    if dist(x, y, x_c, y_c) > r:
        answer = 'NO'
        break
    x, y = [int(s) for s in input().split(',')]

print(answer)
