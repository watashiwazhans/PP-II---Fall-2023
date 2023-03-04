s = str(input())
cnt = 0
cnt2 = 0
for i in s:
    if i.islower():
        cnt += 1  
    if i.isupper():
        cnt2 += 1  
print(cnt, cnt2)
