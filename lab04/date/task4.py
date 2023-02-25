import datetime
x = datetime.datetime.today()
y = datetime.datetime(1959, 9, 1)
delta = x - y
print(f"Time difference in seconds: {delta.total_seconds()}")