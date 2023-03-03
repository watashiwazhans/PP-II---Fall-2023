def ret(a):
    x = a
    while x >= 0:
        yield x
        x -= 1
a = int(input())
for x in ret(a):
    print(x)
