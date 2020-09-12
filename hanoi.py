def move(n, x, y):
    if n == 1:
        print(n, x, y)
    else:
        move(n - 1, x, 6 - x - y)
        print(n, x, y)
        move(n - 1, 6 - x - y, y)

move(int(input()), 1, 3)
