# main.py created inside day 48
# ocal vs global varibles
# (local varibles is detected within a function and is only accessible within that function,it is created when the function is call and destroyed when function returns )
# (global varibles is a variable that defined outside of a function and its accessible from within any function from your code)

x=10              # global variable(outside function)
def my_function():
    y=4            #local variable(within function)
    print(y)
my_function()
print(x) # print global variable

x=10
def my_function():
    global x        # global keyword - this will change the value of global variable
    x=5
    y=4
    print(y)
my_function()
print(x)