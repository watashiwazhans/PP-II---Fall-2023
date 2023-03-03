def squares(a, b):
    x = a
    while x <= b:
        yield x * x
        x += 1
a, b = int(input()), int(input())
for x in squares(a, b):
    print(x)
