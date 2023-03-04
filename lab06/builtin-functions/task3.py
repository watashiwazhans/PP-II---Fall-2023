s = str(input())
t = (''.join(reversed(s)))
if t == s:
    print('yes')
else:
    print('no')