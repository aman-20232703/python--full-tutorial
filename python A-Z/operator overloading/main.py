# main.py created inside day 77
# #77. operator overloading --> Operator Overloading is a feature in Python that allows developers to redefine the behavior of mathematical and comparison operators for custom data types. This means that you can use the standard mathematical operators (+, -, *, /, etc.) and comparison operators (>, <, ==, etc.) in your own classes, just as you would for built-in data types like int, float, and str.

# You can overload an operator in Python by defining special methods in your class. These methods are identified by their names, which start and end with double underscores (__). Here are some of the most commonly overloaded operators and their corresponding special methods:
"""
+ : __add__
- : __sub__
* : __mul__
/ : __truediv__
< : __lt__
> : __gt__
== : __eq__

"""
#e.g- 1

class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
        
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self, x):       # METHOD OVERLOADING
        return f"{self.i + x.i} + {self.j + x.j}j + {self.k + x.k}k"
    
a=vector(3,4,5)
print(a)        #print(str(a))
b=vector(3,6,2)
print(b)
print(a+b)

#e.g- 2
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"{self.x}, {self.y}"

    def __mul__(self, other):        # METHOD OVERLOADING
        return (self.x * other.x, self.y * other.y)
    
a=Point(3,5)
print(a)
b=Point(3,7)
print(b)
print(a*b)
