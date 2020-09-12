def ReadNumbers(n):
    a = []
    for i in range(n - 1):
        a.append(int(input()))
    return a


def IsContains(a, n):
    for i in range(1, n + 1):
        if a == i:
            return True
    return False


def FindLost(a, n):
    for i in range(1, n + 1):
        if i not in a:
            return i


n = int(input())
print(FindLost(ReadNumbers(n), n))
