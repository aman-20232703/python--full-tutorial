#function is a block of code that perform specific task whether it is called, is help reduce same line code uses at diffrent palce by calling function
def gmean(a,b):
    a=(a*b)/(a+b)
    print(a)
    
def greatervalue(a,b):
    if(b>a):
        print("b greater")
    else:
        print("not grater")
        
a=3
b=5
gmean(a,b)
greatervalue(3,5)

def calculator(a,b):
    pass               # this is used when we want to use any function after sometime
    
#two types of function- 1. built-in function(predefined like min(), max(), dict(), list() etc.), 2. user defined function(user need to def...)