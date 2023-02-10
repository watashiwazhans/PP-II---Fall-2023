def check(n):
    if [n[i] for i in range(0, len(n))] == [n[i] for i in range(1, len(n))] == 3:
        print (True)
    else:
        print (False)
n = list(input())
check(n)


