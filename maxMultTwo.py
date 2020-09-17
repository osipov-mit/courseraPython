def MaxMult(a: list):
    temp1 = a[0]
    temp2 = a[1]
    mult = temp1 * temp2
    i = 0
    while i < len(a) - 1:
        t = MultEvery(a[i + 1:], a[i])
        temp1 = a[i] if t * a[i] > mult else temp1
        temp2 = t if t * temp1 > mult else temp2
        mult = temp1 * temp2
        i += 1
    if temp2 > temp1:
        return temp1, temp2
    else:
        return temp2, temp1


def MultEvery(a: list, m):
    res = a[0]
    for i in a[1:]:
        if m * i > m * res:
            res = i
    return res


a = list(map(int, input().split()))
print(*MaxMult(a))

