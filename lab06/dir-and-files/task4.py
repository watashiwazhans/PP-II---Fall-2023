import os
f = open(r"C:\Users\Lenovo\OneDrive\Рабочий стол\PP II\lab06\dir-and-files\sumtext.txt")
cnt = 0
for lines in f:
    cnt += 1
print("files has {} lines".format(cnt))