# decoraters (it is function that takes another function as an argunment and return the new function that modifies the behaviour of the original function )
"""syntax-
@decorator_function
    def my_function():
        pass """

def greet(fx):
    def mfx(*args,**kwargs):         # *args- take argunment as a tuple, **kwargs- take argunment as a dict..
        print("good morning")
        fx(*args,**kwargs)
        print("thanks for using this function")
    return mfx

@greet
def hello():
    print("hello world")

def sum(a,b):
    print(a+b)
    
hello()  #we can also write 'greet(hello)()' then we no need to write @greet like above
greet(sum)(2,3)
