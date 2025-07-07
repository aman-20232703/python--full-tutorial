# main.py created inside day 97
# multithreading (use to download resources paralley)--> Multithreading is a technique in programming that allows multiple threads of execution to run concurrently within a single process. In Python, we can use the threading module to implement multithreading.

import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds      # this is for ThreadPoolExecutor codes
t0=time.time()          #time.perf_counter()
print("time takeen to execute codes",t0)

#1st method
def main():
    # #noraml
    func(2)
    func(3)
    func(4)
    t2=time.time()
    print("time take to execute function",t2)

    print("total time take to execute",t2-t0)
    
    #Functions---The following are some of the most commonly used functions in the threading module:threading.
    # 1. threading.Thread(target, args): This function creates a new thread that runs the target function with the specified arguments.# 2. threading.Lock(): This function creates a lock that can be used to synchronize access to shared resources between threads.
    # using threadiing , 2nd method
    t1=threading.Thread(target=func, args=[2])
    t2=threading.Thread(target=func, args=[3])
    t3=threading.Thread(target=func, args=[4])

    t1.start()
    t2.start()
    t3.start()
    t4=time.time()
    print("time take to threading",t4)
    print("total time take to execute",t4-t0)
# main()
    
#3rd method
# advace concept
def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # future1 = executor.submit(func, 3)
        # future2 = executor.submit(func, 2)
        # future3 = executor.submit(func, 4)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        
    #another method to use threadpoolexecutor
        l = [3, 5, 1, 2]
        results = executor.map(func, l)
        for result in results:
            print(result)

poolingDemo()
