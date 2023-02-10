def check(n):
    for i in range(len(n) - 1):
        if n[i] == 3 and n[i+1] == 3:
            return True
        elif n[i] == 3 and n[i+1] != 3:
                return False
print(check([2, 3, 3]))
print(check([1, 3, 1, 3]))


