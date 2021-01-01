import time

t = time.localtime()
print(t)
print()
print(t.tm_hour)

while True:
    t = time.localtime()
    print(t.tm_year)
    print(t.tm_hour, ":", t.tm_min, ":", t.tm_sec)
    print()
    if(t.tm_year == t.tm_year+1):
        if (t.tm_hour == 00 and t.tm_min == 00 and t.tm_sec == 00):
            print("Happy New Year!!")
            break

