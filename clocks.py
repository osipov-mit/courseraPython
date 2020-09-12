n = int(input())
h = (n // 3600 - 24) % 24
m = (n // 60 - 60) % 60
s = (n % 60 - 60) % 60
mstr = str(m // 10) + str(m % 10)
sstr = str(s // 10) + str(s % 10)
print(h, mstr, sstr, sep=':')
