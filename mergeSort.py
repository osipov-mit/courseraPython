def Merge(a, b):
    res = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    res.extend(a[i:] if len(a) > len(b) else b[j:])
    return res


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*Merge(a, b))
