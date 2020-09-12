n = int(input())
f2 = 0
f1 = 1
fcur = 0
i = 0
while fcur <= n:
    fcur = f2 + f1
    i += 1
    if i == 1 or i == 1:
        continue
    f2 = f1
    f1 = fcur
if f2 == n:
    print(i - 1)
else:
    print(-1)
