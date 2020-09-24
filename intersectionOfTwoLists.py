def Intersection(a, b):
    res = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            res.append(a[i])
            i += 1
            j += 1
    return res


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*Intersection(a, b))
