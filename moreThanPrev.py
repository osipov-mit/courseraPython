def GetMoreThanPrev(a):
    res = []
    temp = a[0]
    for i in a[1:]:
        if i > temp:
            res.append(str(i))
        temp = i
    return res


print(*GetMoreThanPrev(list(map(int, input().split()))))
