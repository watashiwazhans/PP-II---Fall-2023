def even(max):
    x = 0
    while x <= max:
        yield x
        x += 1
n = int(input())
ans = []
for x in even(n):
    if x % 2 == 0:
        ans.append(x)
print(ans)
