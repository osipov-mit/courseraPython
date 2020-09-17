def SamePair(a: list, index: int):
    temp = a[index]
    counter = 0
    for i in a[index+1:]:
        if temp == i:
            counter += 1
    if index < len(a) - 1:
        counter += SamePair(a, index + 1)
    return counter


a = list(map(int, input().split()))
print(SamePair(a, 0))

