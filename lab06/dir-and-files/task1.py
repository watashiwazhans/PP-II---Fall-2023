import os
p = os.listdir(r'C:\Users\Lenovo\OneDrive\Рабочий стол\PP II')
for i in p:
    print(i)
for i in p:
    if os.path.isdir(i) or os.path.isfile(i):
        print(i)
for i in p:
    if os.path.isfile(i):
        print(i)


