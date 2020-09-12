from math import sqrt


def dist(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    return sqrt(x ** 2 + y ** 2)

def IsPointInCircle(x, y, xc, yc, r):
    return dist(x, y, xc, yc) <= r

x, y = float(input()), float(input())
xc, yc = float(input()), float(input())
r = float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print('YES')
else:
    print('NO')
