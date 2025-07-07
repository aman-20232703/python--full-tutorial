# main.py created inside day 30
# recursion(recursion is the process of defining something in terms of itself or function calling within function)
def factorial(n):
    if (n==0 or n==1):      #base value
        return 1
    else:
        return n*factorial(n-1)   #recursive value
print(factorial(5))
# 5*factorial(4)
# 5*4*factorial(3)
# 5*4*3*factorial(2)
# 5*4*3*2*factorial(1)
# 5*4*3*2*1

def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return (n-1)+(n-2)
print(fibonacci(5))
