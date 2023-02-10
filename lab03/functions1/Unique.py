def uni():
    for i in range(len(n) - 1):
        an.append(n[i])
        if n[i] == n[i - 1]:
            an.pop()
    print(an)

a = int(input())
n = []
for i in range (a):
    n.append(int(input()))
an = []
uni()