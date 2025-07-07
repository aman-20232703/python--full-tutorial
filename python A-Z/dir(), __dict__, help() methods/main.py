# main.py created inside day 71
# dir(), __dict__ and help() methods in python--> We must look into dir(), __dict__() and help() attribute/methods in python. They make it easy for us to understand how classes resolve various functions and executes code. In Python, there are three built-in functions that are commonly used to get information about objects: dir(), dict, and help().

# The dir() method--> The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. It is a useful tool for discovering what you can do with an object.
x=[3,5,3]
print(dir(x))
print(x.__add__)

# The __dict__ attribute -->  The __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.salary=3456367
        
p = Person("John", 30)
print(p.__dict__)

# The help() mehthod --> The help() function is used to get help documentation for an object, including a description of its attributes and methods.
print(help(str))
print(help(Person))
