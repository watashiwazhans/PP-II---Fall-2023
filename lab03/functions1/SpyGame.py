def spygame(n):
    mys007 = False
    for i in range(2, len(n) - 1):
        guard = n[i - 2] * 100 + n[i - 1] * 10 + n[i]
        if guard == 7:
            mys007 = True
            break
    return mys007
n = list(map(int, input().split()))
print(spygame(n))

