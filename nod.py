def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def ReduceFraction(n, m):
    nod = gcd(n, m)
    return n // nod, m // nod


a, b = int(input()), int(input())
print(*ReduceFraction(a, b))
