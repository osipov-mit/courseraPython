def Queen(a: list):
    for i in a:
        if DotInList(i, a):
            return 'YES'
    return 'NO'


def DotInList(dot: tuple, a: list):
    i, j = dot[0], dot[1]
    while i < 9 and j > 0:
        i += 1
        j -= 1
        if (i, j) in a:
            return True
    i, j = dot[0], dot[1]
    while j < 9 and i > 0:
        j += 1
        i -= 1
        if (i, j) in a:
            return True
    i, j = dot[0], dot[1]
    while i > 0 and j > 0:
        j -= 2
        i -= 2
        if (i, j) in a:
            return True
    i, j = dot[0], dot[1]
    while i < 9 and j < 9:
        j += 2
        i += 2
        if (i, j) in a:
            return True
    i, j = 0, dot[1]
    while i < 9:
        i += 1
        if (i, j) in a and i != dot[0]:
            return True
    i, j = dot[0], 0
    while j < 9:
        j += 1
        if (i, j) in a and j != dot[1]:
            return True
    return False


def GetListDots():
    a = []
    for i in range(8):
        a.append(tuple(map(int, input().split())))
    return a


print(Queen(GetListDots()))

