def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


a = int(input())
sum = 0
for i in range(1, a + 1):
    sum += fact(i)
print(sum)
