# main.py created inside day 15
# time module
import time
tm=time.strftime("%H:%M:%S")  #strftime is a function which give us hour and minute
print(tm)
tm=time.strftime("%H")
print(tm)
tm=time.strftime("%M")
print(tm)
tm=time.strftime("%S")
print(tm)

# e.g-
import time
tm=int(time.strftime("%H"))
if (tm<12):
    print("good morning")
elif(tm<14 and tm>11):
    print("good afternoon")
elif(tm>14):
    if(tm<18):
        print("good evening")
    else:
        print("goodnight")
else:
    print("not match")