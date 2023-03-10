import os
f = open(r"C:\Users\Lenovo\OneDrive\Рабочий стол\PP II\lab06\dir-and-files\iwrotelist.txt", "a")
a = ["i", "wrote", "some", "stuff"]
for i in a:
    f.write(i)