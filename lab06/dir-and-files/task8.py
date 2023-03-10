import os
p=(r"C:\Users\Lenovo\OneDrive\Рабочий стол\PP II\lab06\dir-and-files\willbedeleted.txt")
if os.path.exists(p):
    os.remove(p)
else:
    print("this file doesnt exist")