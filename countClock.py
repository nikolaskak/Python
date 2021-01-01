import time

t=time.localtime()


newYear = False
while True:
    t=time.localtime()
    print(t.tm_hour, ":", t.tm_min, ":", t.tm_sec)
    print()
    if(t.tm_min==3):

        print("Happy New Year!!")