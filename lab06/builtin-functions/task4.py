from math import * 
import time
a, b = int(input()), int(input())
time.sleep(float(b / 1000))
print('Square root of', a, 'after', b, 'miliseconds is', sqrt(a))
