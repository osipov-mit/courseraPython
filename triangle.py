a = int(input())
b = int(input())
c = int(input())
if c >= a and c >= b:
    maxSide = c
    otherside1 = a
    otherside2 = b
elif a >= c and a >= b:
    maxSide = a
    otherside1 = c
    otherside2 = b
else:
    maxSide = b
    otherside1 = a
    otherside2 = c
if maxSide >= otherside1 + otherside2:
    print('impossible')
elif maxSide ** 2 == otherside1 ** 2 + otherside2 ** 2:
    print('rectangular')
elif maxSide ** 2 < otherside1 ** 2 + otherside2 ** 2:
    print('acute')
else:
    print('obtuse')
