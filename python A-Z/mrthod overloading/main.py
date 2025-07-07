# main.py created inside day 74
# Method Overriding --> Method overriding is a powerful feature in object-oriented programming that allows you to redefine a method in a derived class. The method in the derived class is said to override the method in the base class. When you create an instance of the derived class and call the overridden method, the version of the method in the derived class is executed, rather than the version in the base class.
#e.g- 1
class shape:                # BASE CLASS
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def area(self):
        return self.x*self.y
    
class circle(shape):        # DERIVED CLASS
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)
    
    def area(self):               # override area method
        return 3.14*super().area()
a=shape(3,4)
print(a.area())
b=circle(5)
print(b.area())

#e.g- 2
class Shape:
    def area(self):
        print("Calculating area...")
        
class circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):   # method ovverride
        print("Calculating area of a circle...")
        super().area()
        return 3.14 * self.radius * self.radius
    
b=circle(5)
print(b.area())
        
