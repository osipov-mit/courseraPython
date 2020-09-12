a, b = int(input()), int(input())
c, d = int(input()), int(input())
if a == 0:
    if b == 0:
        print('INF')
    else:
        print('NO')
elif b == 0:
    print(0)
elif c == 0:
    isInt = b % a == 0
    if isInt:
        print(-b // a)
    else:
        print('NO')
elif -b / a != -d / c:
    isInt = b % a == 0
    if isInt:
        print(-b // a)
    else:
        print('NO')
else:
    print('NO')
