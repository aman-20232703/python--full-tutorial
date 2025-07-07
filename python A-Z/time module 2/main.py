# main.py created inside day 84
# time module --> The time module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time conversions. This module is part of the Python Standard Library and is available in all Python installations, making it a convenient and essential tool for a wide range of applications.

#time.time() --> The time.time() function returns the current time as a floating-point number, representing the number of seconds since the epoch (the point in time when the time module was initialized). The returned value is based on the computer's system clock and is affected by time adjustments made by the operating system, such as daylight saving time

import time
# print(time.time())

def usingwhile():
    i=0
    while i<1001:
        print(i)
        i+=1
        
def usingfor():
    for i in range(1001):
        print(i)
        
a=time.time()
usingfor()
t1=time.time()-a

b=time.time()
usingwhile()
t2=time.time()-b

print(t1)
print(t2)

#time.sleep() --> The time.sleep() function suspends the execution of the current thread for a specified number of seconds. This function can be used to pause the program for a certain period of time, allowing other parts of the program to run, or to synchronize the execution of multiple threads
import time

print("print now:", time.time())
time.sleep(3)
print("print after 3s:", time.time())
# Output:
# Start: 1602299933.233374
# End: 1602299935.233376

# time.strftime() --> The time.strftime() function formats a time value as a string, based on a specified format. This function is particularly useful for formatting dates and times in a human-readable format, such as for display in a GUI, a log file,

import time
tm=time.strftime('%Y-%m-%d %H:%M:%S')
print(tm)
