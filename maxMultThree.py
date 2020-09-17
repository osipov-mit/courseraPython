def MaxMult(a: list):
    if len(a) <= 3:
        return a
    tempMax1 = max(a)
    tempMin1 = min(a)
    a.pop(a.index(tempMax1))
    a.pop(a.index(tempMin1))
    tempMax2 = max(a)
    tempMin2 = min(a)
    a.pop(a.index(tempMax2))
    a.pop(a.index(tempMin2))
    if len(a) != 0:
        tempMax3 = max(a)
    else:
        tempMax3 = tempMin2
    multMax = tempMax1 * tempMax2 * tempMax3
    multMin = tempMin1 * tempMin2 * tempMax1
    if multMax > multMin:
        return tempMax1, tempMax2, tempMax3
    else:
        return tempMin1, tempMin2, tempMax1


a = list(map(int, input().split()))
print(*MaxMult(a))

