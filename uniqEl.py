def UniqueElements(a: list):
    res = []
    for i in range(len(a)):
        if a[i] not in a[i+1:] and a[i] not in a[:i]:
            res.append(a[i])
    return res


a = list(map(int, input().split()))
print(*UniqueElements(a))

