def f(mx):
    x = 0
    while x <= mx:
        yield x
        x += 1

n = int(input())
ans = []
for x in f(n):
    if x % 3 == 0 or x % 4 == 0:
        ans.append(x)
print(ans)