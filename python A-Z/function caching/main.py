# main.py created inside day 92
# function caching --> Function caching is a technique for improving the performance of a program by storing the results of a function call so that you can reuse the results instead of recomputing them every time the function is called. This can be particularly useful when a function is computationally expensive, or when the inputs to the function are unlikely to change frequently.
#  function caching can be achieved using the functools.lru_cache decorator
from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(4)
    return n*5

print(fx(2))
print("print done for 2*5\n")
print(fx(5))
print("print done for 5*5\n")
print(fx(8))
print("print done for 8*5\n")

print(fx(2))
print("print done for 2*5\n")
print(fx(5))
print("print done for 5*5\n")
print(fx(8))
print("print done for 8*5\n")

# functools.lru_cache decorator is used to cache the results of the function. The maxsize parameter is used to specify the maximum number of results to cache. If maxsize is set to None, the cache will have an unlimited size

# Benefits of Function Caching--> a significant impact on the performance of a program, particularly for computationally expensive and limited functions. By caching the results of a function, you can avoid having to recompute the results every time the function is called, which can save a significant amount of time and computational resources and storage.

